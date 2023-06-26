import unittest
from deep_translator import MyMemoryTranslator  # Import MyMemoryTranslator

def english_to_french(english_text):
    french_text = MyMemoryTranslator(source="en", target="fr").translate(english_text)
    print(french_text)
    return french_text

class TranslationTests(unittest.TestCase):
    def test_hello_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"

        french_text = english_to_french(english_text)
        self.assertEqual(french_text, expected_french_text)

    def test_bonjour_translation(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"

        english_text = MyMemoryTranslator(source="fr", target="en").translate(french_text)

        self.assertEqual(english_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
    

