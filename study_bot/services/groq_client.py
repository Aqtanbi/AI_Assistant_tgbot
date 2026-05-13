from groq import Groq


class GroqClient:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = Groq(api_key=api_key)
        self.model = model

    def ask_tutor(self, question: str) -> str:
        prompt = (
            "You are a friendly study assistant. "
            "Explain clearly, use simple language, and give a short example.\n\n"
            f"Student question: {question}"
        )
        return self._chat(prompt)

    def create_quiz(self, topic: str, question_count: int = 3) -> str:
        prompt = (
            f"Create {question_count} short quiz questions about {topic}. "
            "Add answers after the questions."
        )
        return self._chat(prompt)

    def _chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You help students learn efficiently."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )
        return response.choices[0].message.content or "No answer received."
