import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    telegram_bot_token: str
    groq_api_key: str
    groq_model: str
    data_folder: str = "data"


def load_config() -> Config:
    load_dotenv()

    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    groq_key = os.getenv("GROQ_API_KEY", "")
    groq_model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    if not telegram_token:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing in .env")

    if not groq_key:
        raise ValueError("GROQ_API_KEY is missing in .env")

    return Config(
        telegram_bot_token=telegram_token,
        groq_api_key=groq_key,
        groq_model=groq_model,
    )
