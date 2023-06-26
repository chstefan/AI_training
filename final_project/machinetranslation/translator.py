"""
This module provides translation functions using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        english_text (str): The English text to translate.

    Returns:
        str: The translated French text.
    """
    french_text = MyMemoryTranslator(source="en", target="fr").translate(english_text)
    print(french_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        french_text (str): The French text to translate.

    Returns:
        str: The translated English text.
    """
    english_text = MyMemoryTranslator(source="fr", target="en").translate(french_text)
    print(english_text)
    return english_text






