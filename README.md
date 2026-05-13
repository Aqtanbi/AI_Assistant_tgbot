# AI-Powered Study Assistant Telegram Bot

This is a simple Python final project: a Telegram bot that helps students study with the Groq AI API.

The project is written in a clear style for learning and defense. It demonstrates basic Python topics, OOP, files, modules, decorators, iterators, generators, regular expressions, and unit tests.

## Features

- Ask an AI study question in Telegram.
- Generate a short quiz about any topic.
- Save favorite notes.
- Show saved notes.
- Track simple study statistics.
- Export study history to CSV.

## Project Structure

```text
FinalProject/
  main.py
  requirements.txt
  .env.example
  data/
    notes.json
    history.csv
  study_bot/
    __init__.py
    bot.py
    config.py
    decorators.py
    iterators.py
    models.py
    services/
      __init__.py
      data_manager.py
      groq_client.py
    utils/
      __init__.py
      text_tools.py
  tests/
    test_data_manager.py
    test_text_tools.py
```

## How To Run

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install libraries:

```bash
pip install -r requirements.txt
```

3. Create `.env` from `.env.example` and fill in your tokens:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

4. Start the bot:

```bash
python main.py
```

## Telegram Commands

- `/start` - welcome message.
- `/help` - show commands.
- `/ask your question` - ask the AI tutor.
- `/quiz topic` - generate a short quiz.
- `/note text` - save a study note.
- `/notes` - show saved notes.
- `/stats` - show study statistics.

## Where Course Topics Are Used

| Course topic | Example in project |
| --- | --- |
| Input/output | Telegram messages and bot replies in `bot.py` |
| Variables and data types | Strings, integers, booleans, lists, dictionaries in many files |
| Arithmetic operators | Statistics calculations in `data_manager.py` |
| Comparison operators | Validation checks in `bot.py` and `text_tools.py` |
| Conditional statements | Command handlers in `bot.py` |
| Logical operators | Text validation in `text_tools.py` |
| Loops | Reading notes/history and formatting output |
| Lists, tuples, sets, dictionaries | `StudySession`, command choices, keyword extraction |
| OS module | Creating the data folder in `data_manager.py` |
| Files, CSV, JSON | `history.csv` and `notes.json` in `data_manager.py` |
| Functions and arguments | Helper functions in `text_tools.py` |
| Lambda, map, filter | `summarize_keywords` in `text_tools.py` |
| OOP classes and objects | `StudyUser`, `StudySession`, `DataManager`, `GroqClient` |
| Inheritance | `QuizSession` inherits from `StudySession` |
| Association | `StudyAssistantBot` uses `DataManager` and `GroqClient` |
| Polymorphism | `describe()` methods in `StudySession` and `QuizSession` |
| Modules and packages | `study_bot/`, `services/`, `utils/` |
| Unit tests | `tests/` folder |
| Decorators | `log_command` in `decorators.py` |
| Iterator | `NoteIterator` in `iterators.py` |
| Generator | `chunk_text` in `text_tools.py` |
| Regular expressions | Cleaning and finding words in `text_tools.py` |

## Running Tests

```bash
python -m unittest discover tests
```

## Defense Explanation

This project solves a real-world study problem: students can ask questions, create quizzes, and save notes directly in Telegram. The Telegram bot is the user interface, Groq is the AI engine, and local JSON/CSV files are used for simple data storage.

The code is split into modules so each file has one clear responsibility. This makes the project easier to explain and maintain.
