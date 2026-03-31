import torch
import numpy as np

class AEQMonitor:
    def __init__(self, vocab_size, tau_base=0.85, window_size=3):
        self.vocab_size = vocab_size
        self.tau_base = tau_base
        self.window_size = window_size
        self.entropy_history = []
        self.halt_count = 0
        self.cooldown_counter = 0
        self.state = "NORMAL"  # States: NORMAL, POST_INTERVENTION, COOLDOWN

    def get_normalized_entropy(self, logits):
        """Normalization: Ensures the threshold works for any model size."""
        probs = torch.softmax(logits, dim=-1)
        H = -torch.sum(probs * torch.log(probs + 1e-10), dim=-1)
        H_normalized = H / np.log(self.vocab_size)
        return H_normalized

    def update_and_check(self, logits, domain="factual"):
        # Calculate smoothed entropy using the Sliding Window
        current_h = self.get_normalized_entropy(logits)
        self.entropy_history.append(current_h)
        if len(self.entropy_history) > self.window_size:
            self.entropy_history.pop(0)
        
        smoothed_h = sum(self.entropy_history) / len(self.entropy_history)

        # 1. COOLDOWN RECOVERY LOGIC
        if self.state == "COOLDOWN":
            recovery_threshold = self.tau_base * 0.5 # Wait for "Deep Calm"
            
            if smoothed_h < recovery_threshold:
                self.cooldown_counter += 1
            else:
                self.cooldown_counter = 0 

            if self.cooldown_counter >= 50: # Stabilization Window (M=50)
                self.state = "NORMAL"
                self.halt_count = 0
                return "REACTIVATE_MONITOR", smoothed_h
            
            return "PASSIVE_MONITOR", smoothed_h

        # 2. SKIP MONITORING DURING INTERVENTION
        if self.state == "POST_INTERVENTION":
            return "PASSIVE_MONITORING", smoothed_h

        # 3. INTERVENTION LOGIC
        tau = self.tau_base if domain == "factual" else self.tau_base + 0.1
        
        if self.state == "NORMAL" and smoothed_h > tau:
            self.halt_count += 1
            
            # Cascade Prevention: If 2 halts happen fast, go to COOLDOWN
            if self.halt_count >= 2:
                self.state = "COOLDOWN"
                self.cooldown_counter = 0
                return "TRIGGER_COOLDOWN", smoothed_h
            
            return "TRIGGER_HALT", smoothed_h

        return "PROCEED", smoothed_h
