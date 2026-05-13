import csv
import json
import os
from datetime import datetime


class DataManager:
    def __init__(self, data_folder: str = "data") -> None:
        self.data_folder = data_folder
        self.notes_path = os.path.join(data_folder, "notes.json")
        self.history_path = os.path.join(data_folder, "history.csv")
        self._prepare_files()

    def _prepare_files(self) -> None:
        os.makedirs(self.data_folder, exist_ok=True)

        if not os.path.exists(self.notes_path):
            with open(self.notes_path, "w", encoding="utf-8") as file:
                json.dump([], file)

        if not os.path.exists(self.history_path):
            with open(self.history_path, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["time", "user_id", "action", "text"])

    def save_note(self, user_id: int, text: str) -> None:
        notes = self.load_notes(user_id=None)
        notes.append(
            {
                "user_id": user_id,
                "text": text,
                "created_at": datetime.now().isoformat(timespec="seconds"),
            }
        )

        with open(self.notes_path, "w", encoding="utf-8") as file:
            json.dump(notes, file, indent=2)

    def load_notes(self, user_id: int | None) -> list[dict]:
        with open(self.notes_path, "r", encoding="utf-8") as file:
            notes = json.load(file)

        if user_id is None:
            return notes

        return [note for note in notes if note["user_id"] == user_id]

    def save_history(self, user_id: int, action: str, text: str) -> None:
        with open(self.history_path, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [datetime.now().isoformat(timespec="seconds"), user_id, action, text]
            )

    def get_stats(self, user_id: int) -> dict:
        total_actions = 0
        ask_count = 0
        quiz_count = 0

        with open(self.history_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["user_id"]) == user_id:
                    total_actions += 1

                    if row["action"] == "ask":
                        ask_count += 1
                    elif row["action"] == "quiz":
                        quiz_count += 1

        note_count = len(self.load_notes(user_id))
        active_score = total_actions + note_count * 2

        return {
            "total_actions": total_actions,
            "ask_count": ask_count,
            "quiz_count": quiz_count,
            "note_count": note_count,
            "active_score": active_score,
        }
