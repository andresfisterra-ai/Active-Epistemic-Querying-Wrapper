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
