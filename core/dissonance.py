import torch
import numpy as np

class AEQMonitor:
    def __init__(self, vocab_size, tau_base=0.85, window_size=3):
        self.vocab_size = vocab_size
        self.tau_base = tau_base
        self.window_size = window_size
        self.entropy_history = []
        self.halt_count = 0
        self.state = "NORMAL"  # States: NORMAL, POST_INTERVENTION, COOLDOWN

    def get_normalized_entropy(self, logits):
        """Normalization: Comparing entropy across models regardless of size."""
        probs = torch.softmax(logits, dim=-1)
        # Shannon Entropy calculation
        H = -torch.sum(probs * torch.log(probs + 1e-10), dim=-1)
        # Normalize by log(vocab_size) to keep values between 0 and 1
        H_normalized = H / np.log(self.vocab_size)
        return H_normalized

    def update_and_check(self, logits, domain="factual"):
        # 1. State-Aware Check: Skip monitoring during intervention
        if self.state == "POST_INTERVENTION":
            return "PASSIVE_MONITOR", 0.0

        # 2. Mathematical Smoothing: Sliding window to reduce noise
        current_h = self.get_normalized_entropy(logits)
        self.entropy_history.append(current_h)
        if len(self.entropy_history) > self.window_size:
            self.entropy_history.pop(0)
        
        smoothed_h = sum(self.entropy_history) / len(self.entropy_history)

        # 3. Dynamic Threshold Tuning (Tau)
        # Lower tau for factual precision; Higher tau for creative domains.
        tau = self.tau_base if domain == "factual" else self.tau_base + 0.1

        # 4. Intervention Logic with Cascade Prevention[cite: 1]
        if self.state == "NORMAL" and smoothed_h > tau:
            self.halt_count += 1
            if self.halt_count >= 2: # Detect cascade[cite: 1]
                self.state = "COOLDOWN"
                return "TRIGGER_COOLDOWN", smoothed_h
            
            # Phase 2: Distinguish Informational vs. Value[cite: 1]
            # Placeholder for classification logic
            return "TRIGGER_HALT_VALUE", smoothed_h

        return "PROCEED", smoothed_h
