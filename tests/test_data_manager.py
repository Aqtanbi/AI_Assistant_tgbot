import tempfile
import unittest

from study_bot.services.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def test_save_and_load_note(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            manager = DataManager(folder)
            manager.save_note(user_id=1, text="Study Python dictionaries")

            notes = manager.load_notes(user_id=1)

            self.assertEqual(len(notes), 1)
            self.assertEqual(notes[0]["text"], "Study Python dictionaries")

    def test_stats_count_actions(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            manager = DataManager(folder)
            manager.save_history(user_id=1, action="ask", text="What is Python?")
            manager.save_history(user_id=1, action="quiz", text="loops")
            manager.save_note(user_id=1, text="Remember for loops")

            stats = manager.get_stats(user_id=1)

            self.assertEqual(stats["total_actions"], 2)
            self.assertEqual(stats["ask_count"], 1)
            self.assertEqual(stats["quiz_count"], 1)
            self.assertEqual(stats["note_count"], 1)
            self.assertEqual(stats["active_score"], 4)


if __name__ == "__main__":
    unittest.main()
