### Adding a New Language/Domain
1. **Check for duplicates**: Search the `lexicon.json` for your language/domain.
2. **Follow the template**:
   ```json
   {
     "[language_code]": {
       "domains": {
         "[domain]": {
           "high_dissonance": "[phrase]",
           "moderate_dissonance": "[phrase]",
           "cultural_notes": "[e.g., 'Latin American Spanish; collaborative tone']"
         }
       }
     }
   }

Lexicon Integration

Dynamic lexicon selection:

Match the uncertainty phrase to:

Model confidence (e.g., “I’m 30% confident” vs. “I’m torn”).
User’s language/domain (from their profile or prompt metadata).

def select_lexicon_entry(model_confidence, user_language, domain):
    if model_confidence < 0.2:
        return lexicon[user_language][domain]["critical_uncertainty"]
    else:
        return lexicon[user_language][domain]["moderate_uncertainty"]
