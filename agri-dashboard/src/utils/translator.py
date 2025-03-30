from typing import Dict, Any
import json
import os

class Translator:
    def __init__(self):
        self.translations = self._load_translations()
        self.current_language = "English"
    
    def _load_translations(self) -> Dict[str, Dict[str, str]]:
        """Load translation files for supported languages"""
        translations_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'translations')
        translations = {}
        
        for filename in os.listdir(translations_dir):
            if filename.endswith('.json'):
                language = filename.split('.')[0]
                with open(os.path.join(translations_dir, filename), 'r', encoding='utf-8') as f:
                    translations[language] = json.load(f)
        
        return translations
    
    def set_language(self, language: str) -> None:
        """Set the current language for translations"""
        if language in self.translations:
            self.current_language = language
        else:
            raise ValueError(f"Language {language} not supported")
    
    def translate(self, key: str) -> str:
        """Get translation for a given key in current language"""
        try:
            return self.translations[self.current_language][key]
        except KeyError:
            return key  # Fallback to key if translation not found