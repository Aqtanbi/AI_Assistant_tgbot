from study_bot.bot import StudyAssistantBot
from study_bot.config import load_config


def main() -> None:
    config = load_config()
    bot = StudyAssistantBot(config)
    bot.run()


if __name__ == "__main__":
    main()
