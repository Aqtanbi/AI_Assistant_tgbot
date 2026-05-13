import unittest

from study_bot.utils.text_tools import clean_text, find_keywords, is_valid_study_text


class TestTextTools(unittest.TestCase):
    def test_clean_text_removes_extra_spaces(self) -> None:
        self.assertEqual(clean_text("  hello    world  "), "hello world")

    def test_valid_study_text(self) -> None:
        self.assertTrue(is_valid_study_text("Python loops"))
        self.assertFalse(is_valid_study_text(""))
        self.assertFalse(is_valid_study_text("ab"))

    def test_find_keywords(self) -> None:
        keywords = find_keywords("Python is great for study and practice.")
        self.assertTrue("python" in keywords)
        self.assertFalse("is" in keywords)


if __name__ == "__main__":
    unittest.main()
