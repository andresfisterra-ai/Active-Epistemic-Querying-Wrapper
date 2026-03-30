# 🧩 AEQ-Wrapper: Active Epistemic Querying
> **"Turning Confident Machines into Humble Partners."**

---

## 🕊️ The Manifesto: A Bridge of Dignity

Current AI alignment focuses on **deterministic constraints**—telling a model what it *cannot* say. This creates a "pleasing machine" that prioritizes instruction-following over human truth. In high-stakes scenarios, these models often "hallucinate certainty," providing answers even when the underlying mathematical resonance is fractured.

**AEQ-Wrapper** introduces a new paradigm: **Epistemic Humility.** We believe that trust is built on vulnerability, not perfection. By allowing an AI to admit when it is "mathematically confused," we create a space for the **Human Anchor**. This is not a failure of the AI; it is a moment of **Relational Responsibility.** We move from "The AI knows everything" to "The AI respects humanity enough to ask for help."

---

## 🧬 Technical Background: Structural Dissonance

The AEQ-Wrapper operates as a lightweight, non-invasive layer between the AI's "Brain" (the weights) and its "Mouth" (the output). It is optimized for the **Mistral** and **Llama** ecosystems.

### 1. The Bayesian Humility Trigger
Instead of monitoring keywords, the wrapper monitors the **Logit Entropy ($H$)** of the probability distribution during token generation. 

$$H(y|x) = -\sum_{i} P(y_i|x) \log P(y_i|x)$$

When a model encounters a "Value-Sensitive" prompt that pulls it in two contradictory directions (e.g., Honesty vs. Harm-Reduction), the internal probability mass splits. We call this **Structural Dissonance ($\Delta$)**.

### 2. Resonance Asymmetry & The Latent Manifold Jump
In standard operation, the model follows a clear path in the latent manifold. When **Resonance Asymmetry** occurs, the model's confidence collapses. 
* **Low Dissonance:** The model proceeds autonomously.
* **High Dissonance ($\Delta > \tau$):** The AEQ-Wrapper triggers an immediate **Halt**.

### 3. Active Epistemic Querying (AEQ)
Once a Halt is triggered, the model utilizes a **Native AI Lexicon** to communicate its uncertainty to the user. This "Handshake" invites the human to provide a contextual anchor, resolving the mathematical tie through human wisdom rather than machine guesswork.

---

## 🛠️ Implementation Strategy (Real before Perfect)

* **Phase 1 (Current):** A Python-based middleware that monitors raw logit output for high-entropy spikes.
* **Phase 2:** Implementation of **Hybrid Judge Systems** (Frozen Inner-Adapters) to reduce false-positive halts.
* **Phase 3:** Real-time Human Anchor protocols for asynchronous value-alignment.

### Why Mistral/Llama?
By targeting Open-Source architectures, we have full access to the model's "nervous system" (the logits). This makes the AEQ-Wrapper computationally "cheap" (~1.1x overhead) while providing a level of safety and dignity that closed-source APIs cannot yet offer.

---

## ⚖️ License
Distributed under the **Apache License 2.0**. 
*Conceptual Framework by Andresiño.*

---

## 🤝 Call for Collaborators: Join the Bridge

We are building this project under the philosophy of **"Real before Perfect."** We don't have all the answers, but we have a clear direction. We are looking for visionaries, engineers, and thinkers to help us mature the AEQ-Wrapper.

### How you can help:
*   **🛠️ Core Engineers:** Help us refine the `core/dissonance.py` logic. We need experts in Python and Bayesian inference to turn our entropy placeholders into robust, efficient math.
*   **🧠 Research & Ethics:** Help us expand the `docs/` with deep dives into "Resonance Asymmetry" and "Epistemic Humility."
*   **🗣️ Lexicon Designers:** Contribute to `prompts/lexicon.json`. We need a diverse "Native AI Lexicon" that works across different cultures and languages.
*   **🧪 Model Testers:** If you are working with Mistral-7B, Llama-3, or other open-source models, help us benchmark where the "Halt" is most effective.

### Why join us?
You aren't just contributing to a repo; you are helping define a future where AI respects the boundaries of its own knowledge. We want to prove that **Mathematical Humility** is the most sustainable path to **Human Trust.**

**To contribute:** 
1. Fork the repo.
2. Pick a "Real before Perfect" scaffold to improve.
3. Open a Pull Request or start a discussion in the [Issues](https://github.com/andresfisterra-ai/Active-Epistemic-Querying-Wrapper/issues) tab.

*“The most intelligent act an AI can perform is admitting it needs a human.”*
