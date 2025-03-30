import pytest
from src.utils.translator import Translator

@pytest.fixture
def translator():
    return Translator()

def test_translator_initialization(translator):
    assert translator.current_language == "English"
    assert isinstance(translator.translations, dict)

def test_language_change(translator):
    translator.set_language("Hindi")
    assert translator.current_language == "Hindi"
    
    with pytest.raises(ValueError):
        translator.set_language("InvalidLanguage")

def test_translation(translator):
    # Test with existing key
    assert translator.translate("weather") != "weather"
    
    # Test with non-existing key
    assert translator.translate("nonexistent_key") == "nonexistent_key"