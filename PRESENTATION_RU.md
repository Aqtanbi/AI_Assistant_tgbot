# Презентация: AI-Powered Study Assistant Telegram Bot

## Слайд 1. Тема проекта

**AI-Powered Study Assistant Telegram Bot**

Python final project  
Telegram Bot + Groq API

## Слайд 2. Проблема

Студентам часто нужна быстрая помощь во время учебы:

- объяснить сложную тему;
- получить пример;
- создать quiz для самопроверки;
- сохранить важную заметку.

## Слайд 3. Решение

Я создал Telegram-бота, который работает как AI study assistant.

Бот помогает студенту:

- задавать вопросы;
- получать AI-ответы;
- создавать quiz;
- сохранять заметки;
- смотреть статистику.

## Слайд 4. Используемые технологии

- Python
- Telegram Bot API
- Groq API
- JSON
- CSV
- unittest
- Git and GitHub

## Слайд 5. Команды бота

- `/start` - welcome message
- `/help` - command list
- `/ask` - ask AI tutor
- `/quiz` - generate quiz
- `/note` - save note
- `/notes` - show notes
- `/stats` - show statistics

## Слайд 6. Архитектура проекта

Основные части проекта:

- `main.py` - запуск приложения
- `bot.py` - Telegram commands
- `groq_client.py` - Groq API
- `data_manager.py` - JSON and CSV files
- `models.py` - OOP classes
- `tests/` - unit tests

## Слайд 7. Работа с Groq API

Пользователь пишет вопрос в Telegram.

Бот отправляет вопрос в Groq API.

Groq возвращает AI-generated answer.

Бот отправляет ответ пользователю.

## Слайд 8. Работа с данными

Проект сохраняет данные локально:

- `notes.json` - saved notes
- `history.csv` - user actions

Это показывает работу с files, JSON, CSV and OS module.

## Слайд 9. OOP в проекте

В проекте используются classes and objects:

- `StudyAssistantBot`
- `DataManager`
- `GroqClient`
- `StudyUser`
- `StudySession`
- `QuizSession`

Также есть inheritance, association and polymorphism.

## Слайд 10. Другие темы Python

Проект демонстрирует:

- variables and data types
- if/elif/else
- loops
- lists, dictionaries, sets
- functions
- lambda, map, filter
- decorators
- iterators
- generators
- regular expressions

## Слайд 11. Testing

Для проверки проекта используются unit tests.

Команда запуска:

```bash
python -m unittest discover tests
```

Тесты проверяют text tools and data manager.

## Слайд 12. Conclusion

Проект показывает, как Python можно использовать для создания real-world application.

Bot is useful, easy to understand, and demonstrates all main course topics.
