This is the default folder for the WordWeaver backend.

To modify this folder for your language, please do the following:
    1. Rename this folder to your language's ISO 639-3 code.
    2. Add your four JSON data files (verbs, pronouns, options, and conjugations).
    3. Using the CLI, generate your data's internationalization files into the i18n folder.

Don't forget to change the WWLANG varilable to your languages ISO 639-3 code in the `./env-backend.env` file.

Congrats! Your WordWeaver backend is complete :)
