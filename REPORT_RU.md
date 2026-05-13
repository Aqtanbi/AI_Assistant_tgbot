# Отчет по финальному проекту

## AI-Powered Study Assistant Telegram Bot

**Студент:** Aqsh  
**Тема проекта:** AI-Powered Study Assistant Telegram Bot  
**Язык программирования:** Python  
**Используемые технологии:** Telegram Bot API, Groq API, JSON, CSV, unittest

## 1. Введение

В современном обучении студентам часто нужна быстрая помощь: объяснение темы, примеры, вопросы для самопроверки и место для сохранения заметок. Поэтому был разработан Telegram-бот **AI-Powered Study Assistant**, который помогает студенту учиться прямо в Telegram.

Пользователь может задавать вопросы, создавать короткие quiz-задания, сохранять заметки и смотреть статистику своей активности. Для генерации ответов используется Groq API, а для хранения данных используются локальные файлы JSON и CSV.

## 2. Цель проекта

Цель проекта - создать практическое Python-приложение, которое демонстрирует основные темы курса и решает реальную учебную задачу.

Основные задачи проекта:

- создать Telegram-бота;
- подключить Groq API для AI-ответов;
- реализовать команды для учебной помощи;
- сохранять заметки пользователя;
- сохранять историю действий;
- показать использование тем курса Python;
- добавить unit tests.

## 3. Функциональные возможности

Бот поддерживает следующие команды:

- `/start` - приветствие пользователя;
- `/help` - список доступных команд;
- `/ask question` - задать вопрос AI-ассистенту;
- `/quiz topic` - создать короткий quiz по теме;
- `/note text` - сохранить заметку;
- `/notes` - показать сохраненные заметки;
- `/stats` - показать статистику обучения.

## 4. Архитектура проекта

Проект разделен на несколько модулей, чтобы код было легче читать, объяснять и поддерживать.

```text
FinalProject/
  main.py
  README.md
  DEFENSE_GUIDE_RU.md
  REPORT_RU.md
  requirements.txt
  data/
    notes.json
    history.csv
  study_bot/
    bot.py
    config.py
    decorators.py
    iterators.py
    models.py
    services/
      data_manager.py
      groq_client.py
    utils/
      text_tools.py
  tests/
    test_data_manager.py
    test_text_tools.py
```

### Описание основных файлов

`main.py` - точка запуска приложения. Загружает настройки и запускает бота.

`study_bot/bot.py` - основной класс Telegram-бота. Здесь находятся обработчики команд.

`study_bot/config.py` - загрузка настроек из `.env`.

`study_bot/services/groq_client.py` - класс для работы с Groq API.

`study_bot/services/data_manager.py` - класс для сохранения заметок и истории в файлы.

`study_bot/models.py` - классы пользователя и учебных сессий.

`study_bot/utils/text_tools.py` - функции для обработки текста.

`tests/` - unit tests для проверки функций и работы с данными.

## 5. Использованные темы Python

### Introduction to Python and Basic Programming Concepts

В проекте используются базовые элементы Python: переменные, строки, числа, типы данных, ввод и вывод. Вводом являются сообщения пользователя в Telegram, а выводом - ответы бота.

Пример:

```python
message = "Hello, student!"
await update.message.reply_text(message)
```

### Control Flow and Looping

Условные операторы используются для проверки корректности команд. Циклы используются при чтении истории, подсчете статистики и выводе заметок.

Пример:

```python
if not is_valid_study_text(question):
    await update.message.reply_text("Please write a question after /ask.")
    return
```

### Collections

В проекте используются списки, словари и множества:

- list - список заметок;
- dict - одна заметка или статистика;
- set - уникальные keywords;
- tuple можно использовать для неизменяемых наборов команд или настроек.

### Files and Data Formats

Проект работает с файлами:

- `notes.json` - хранит заметки пользователя;
- `history.csv` - хранит историю действий;
- `os.makedirs()` - создает папку `data`, если ее нет.

### Functions

Функции используются для разделения логики на маленькие понятные части. Например, `clean_text()` очищает лишние пробелы, а `is_valid_study_text()` проверяет текст.

В проекте также есть `lambda`, `map` и `filter` в функции `summarize_keywords()`.

### Object-Oriented Programming

Проект использует классы:

- `StudyAssistantBot`;
- `DataManager`;
- `GroqClient`;
- `StudyUser`;
- `StudySession`;
- `QuizSession`.

Класс помогает объединить данные и методы, которые относятся к одной части программы.

### Advanced OOP

В проекте есть наследование: `QuizSession` наследуется от `StudySession`.

Также есть polymorphism: оба класса имеют метод `describe()`, но возвращают разный текст.

Association показана в классе `StudyAssistantBot`: он использует объекты `DataManager` и `GroqClient`.

### Modules and Packages

Папка `study_bot` является Python package. Код разделен на модули и подпакеты:

- `services`;
- `utils`;
- `models`;
- `bot`.

Это делает проект более структурированным.

### Decorators

В файле `decorators.py` реализован decorator `log_command`, который выводит в терминал информацию о начале и завершении команды.

Пример:

```python
@log_command("ask")
async def ask(...):
    ...
```

### Iterator

В файле `iterators.py` реализован custom iterator `NoteIterator`. Он использует методы `__iter__()` и `__next__()`, а также `StopIteration`.

### Generator

Функция `chunk_text()` использует `yield`, чтобы делить длинные ответы AI на части. Это нужно, потому что Telegram имеет ограничения на длину сообщения.

### Regular Expressions

В файле `text_tools.py` используется модуль `re`:

- `re.sub()` - очистка лишних пробелов;
- `re.findall()` - поиск слов и keywords.

### Unit Tests

Для проверки проекта используются unit tests:

```bash
python -m unittest discover tests
```

Тесты проверяют обработку текста и сохранение данных.

## 6. Работа с Groq API

Groq API используется как AI engine. Пользователь отправляет вопрос в Telegram, бот передает этот вопрос в класс `GroqClient`, а затем Groq возвращает ответ.

Основная логика находится в файле `study_bot/services/groq_client.py`.

Преимущество такого подхода: если в будущем нужно заменить AI provider, достаточно изменить один файл, а не весь проект.

## 7. Работа с данными

Данные сохраняются локально:

- заметки хранятся в JSON;
- история действий хранится в CSV.

Такой подход простой и понятный для учебного проекта. Он показывает работу с файлами и форматами данных без сложной базы данных.

## 8. Тестирование

Проект содержит unit tests в папке `tests`.

Проверяются:

- очистка текста;
- проверка валидности текста;
- поиск keywords;
- сохранение и загрузка заметок;
- подсчет статистики.

Результат запуска тестов:

```text
Ran 5 tests
OK
```

## 9. Инструкция по запуску

1. Установить зависимости:

```bash
pip install -r requirements.txt
```

2. Создать файл `.env`:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

3. Запустить проект:

```bash
python main.py
```

4. Открыть Telegram-бота и протестировать команды.

## 10. Заключение

В результате был создан Telegram-бот для помощи в обучении. Проект показывает, как Python можно использовать для создания реального приложения с AI API, обработкой пользовательских команд, хранением данных и тестированием.

Проект соответствует темам курса: базовый Python, условия, циклы, коллекции, файлы, функции, OOP, наследование, модули, decorators, iterators, generators, regular expressions и unit tests.

## 11. Список использованных источников

- Python Documentation: https://docs.python.org/3/
- python-telegram-bot Documentation: https://docs.python-telegram-bot.org/
- Groq Documentation: https://console.groq.com/docs/
- GitHub Documentation: https://docs.github.com/
