# Гайд для защиты проекта

## Тема проекта

**AI-Powered Study Assistant Telegram Bot** - это Telegram-бот, который помогает студенту учиться с помощью AI через Groq API.

Пользователь пишет команду в Telegram, бот обрабатывает сообщение, обращается к Groq API и возвращает ответ. Также бот умеет сохранять заметки и вести простую статистику обучения.

## Почему проект полезный

Студенту не нужно открывать отдельный сайт или приложение. Он может прямо в Telegram:

- задать вопрос по учебной теме;
- получить короткое объяснение;
- создать quiz;
- сохранить заметку;
- посмотреть историю активности.

## Основные файлы

- `main.py` - точка запуска проекта.
- `study_bot/bot.py` - Telegram-команды и логика общения с пользователем.
- `study_bot/services/groq_client.py` - работа с Groq API.
- `study_bot/services/data_manager.py` - сохранение JSON и CSV файлов.
- `study_bot/models.py` - классы пользователя и учебных сессий.
- `study_bot/utils/text_tools.py` - функции для обработки текста.
- `study_bot/decorators.py` - пример decorator.
- `study_bot/iterators.py` - пример custom iterator.
- `tests/` - unit tests.

## Как объяснить архитектуру

Проект разделен на модули, потому что так код легче читать и поддерживать.

`StudyAssistantBot` не хранит данные сам. Он использует `DataManager`. Это называется association: один класс использует объект другого класса.

`StudyAssistantBot` также использует `GroqClient`, чтобы не писать код API прямо внутри Telegram-команд.

## Где использованы темы курса

1. **Variables and data types**
   Используются строки, числа, списки, словари и boolean-проверки.

2. **Input and output**
   Input - сообщения пользователя в Telegram. Output - ответы бота.

3. **Arithmetic operators**
   В `DataManager.get_stats()` считается `active_score`.

4. **Comparison operators**
   Валидация текста: проверяем длину строки и количество заметок.

5. **Conditional statements**
   `if`, `elif`, `else` используются при проверке команд и статистики.

6. **Logical operators**
   В `is_valid_study_text()` используется `and` и `not`.

7. **Loops**
   `for` используется для вывода заметок и чтения CSV.

8. **Collections**
   Lists используются для заметок, dictionaries для JSON-данных, sets для keywords, tuples можно объяснить как неизменяемую структуру для команд или настроек.

9. **Files, OS, CSV, JSON**
   `os.makedirs()` создает папку `data`.
   `notes.json` хранит заметки.
   `history.csv` хранит историю действий.

10. **Functions**
    В проекте много функций: `clean_text`, `find_keywords`, `load_config`.

11. **Lambda, map, filter**
    Используются в `summarize_keywords()`.

12. **OOP**
    Есть классы `StudyUser`, `StudySession`, `QuizSession`, `DataManager`, `GroqClient`.

13. **Inheritance**
    `QuizSession` наследуется от `StudySession`.

14. **Polymorphism**
    У `StudySession` и `QuizSession` есть метод `describe()`, но работает он по-разному.

15. **Modules and packages**
    Папка `study_bot` является Python package, внутри есть модули и подпакеты.

16. **Unit tests**
    Тесты находятся в папке `tests`.

17. **Decorators**
    `@log_command` показывает начало и конец выполнения команды.

18. **Iterator**
    `NoteIterator` реализует `__iter__()` и `__next__()`.

19. **Generator**
    `chunk_text()` использует `yield`, чтобы делить длинный ответ на части.

20. **Regular expressions**
    `re.sub()` чистит пробелы, `re.findall()` ищет слова.

## Что сказать про Groq API

Groq API используется как AI engine. В файле `groq_client.py` есть класс `GroqClient`, который отправляет prompt и получает ответ от модели.

Это удобно, потому что если позже нужно поменять AI provider, мы меняем только этот файл, а не весь проект.

## Как запустить на защите

1. Установить библиотеки:

```bash
pip install -r requirements.txt
```

2. Создать `.env`:

```text
TELEGRAM_BOT_TOKEN=your_token
GROQ_API_KEY=your_key
GROQ_MODEL=llama-3.1-8b-instant
```

3. Запустить:

```bash
python main.py
```

4. Проверить тесты:

```bash
python -m unittest discover tests
```

## Короткая речь

My project is an AI-powered study assistant Telegram bot. It helps students ask questions, generate quizzes, save notes, and track study statistics. The bot uses Telegram as the user interface, Groq API as the AI engine, and local JSON/CSV files for data storage. I divided the code into modules to make the project easier to read, test, and maintain. The project demonstrates Python basics, control flow, collections, files, functions, OOP, inheritance, modules, decorators, iterators, generators, regular expressions, and unit testing.
