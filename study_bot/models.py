from dataclasses import dataclass
from datetime import datetime


@dataclass
class StudyUser:
    user_id: int
    username: str

    def display_name(self) -> str:
        if self.username:
            return self.username
        return f"student-{self.user_id}"


class StudySession:
    def __init__(self, user: StudyUser, topic: str) -> None:
        self.user = user
        self.topic = topic
        self.created_at = datetime.now()

    def describe(self) -> str:
        return f"{self.user.display_name()} studied '{self.topic}'"


class QuizSession(StudySession):
    def __init__(self, user: StudyUser, topic: str, question_count: int = 3) -> None:
        super().__init__(user, topic)
        self.question_count = question_count

    def describe(self) -> str:
        return (
            f"{self.user.display_name()} requested a {self.question_count}-question "
            f"quiz about '{self.topic}'"
        )
