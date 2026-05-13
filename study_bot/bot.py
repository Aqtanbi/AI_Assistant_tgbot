from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from study_bot.config import Config
from study_bot.decorators import log_command
from study_bot.iterators import NoteIterator
from study_bot.models import QuizSession, StudySession, StudyUser
from study_bot.services.data_manager import DataManager
from study_bot.services.groq_client import GroqClient
from study_bot.utils.text_tools import chunk_text, clean_text, is_valid_study_text


class StudyAssistantBot:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.data_manager = DataManager(config.data_folder)
        self.groq_client = GroqClient(config.groq_api_key, config.groq_model)

    def run(self) -> None:
        app = Application.builder().token(self.config.telegram_bot_token).build()

        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("help", self.help))
        app.add_handler(CommandHandler("ask", self.ask))
        app.add_handler(CommandHandler("quiz", self.quiz))
        app.add_handler(CommandHandler("note", self.note))
        app.add_handler(CommandHandler("notes", self.notes))
        app.add_handler(CommandHandler("stats", self.stats))

        print("Study Assistant Bot is running...")
        app.run_polling()

    def _get_user(self, update: Update) -> StudyUser:
        telegram_user = update.effective_user
        username = telegram_user.username if telegram_user and telegram_user.username else ""
        user_id = telegram_user.id if telegram_user else 0
        return StudyUser(user_id=user_id, username=username)

    def _get_command_text(self, context: ContextTypes.DEFAULT_TYPE) -> str:
        return clean_text(" ".join(context.args))

    @log_command("start")
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        message = (
            f"Hello, {user.display_name()}!\n\n"
            "I am your AI-powered study assistant.\n"
            "Use /ask, /quiz, /note, /notes, and /stats."
        )
        await update.message.reply_text(message)

    @log_command("help")
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = (
            "Commands:\n"
            "/ask your question - ask the AI tutor\n"
            "/quiz topic - create a short quiz\n"
            "/note text - save a note\n"
            "/notes - show saved notes\n"
            "/stats - show your study statistics"
        )
        await update.message.reply_text(message)

    @log_command("ask")
    async def ask(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        question = self._get_command_text(context)

        if not is_valid_study_text(question):
            await update.message.reply_text("Please write a question after /ask.")
            return

        session = StudySession(user, question)
        print(session.describe())

        self.data_manager.save_history(user.user_id, "ask", question)
        answer = self.groq_client.ask_tutor(question)

        for part in chunk_text(answer):
            await update.message.reply_text(part)

    @log_command("quiz")
    async def quiz(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        topic = self._get_command_text(context)

        if not is_valid_study_text(topic):
            await update.message.reply_text("Please write a topic after /quiz.")
            return

        session = QuizSession(user, topic, question_count=3)
        print(session.describe())

        self.data_manager.save_history(user.user_id, "quiz", topic)
        quiz_text = self.groq_client.create_quiz(topic, question_count=3)

        for part in chunk_text(quiz_text):
            await update.message.reply_text(part)

    @log_command("note")
    async def note(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        text = self._get_command_text(context)

        if not is_valid_study_text(text):
            await update.message.reply_text("Please write note text after /note.")
            return

        self.data_manager.save_note(user.user_id, text)
        self.data_manager.save_history(user.user_id, "note", text)
        await update.message.reply_text("Note saved.")

    @log_command("notes")
    async def notes(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        notes = self.data_manager.load_notes(user.user_id)

        if len(notes) == 0:
            await update.message.reply_text("You do not have saved notes yet.")
            return

        lines = []
        for number, note in enumerate(NoteIterator(notes), start=1):
            lines.append(f"{number}. {note['text']} ({note['created_at']})")

        await update.message.reply_text("\n".join(lines))

    @log_command("stats")
    async def stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = self._get_user(update)
        stats = self.data_manager.get_stats(user.user_id)
        message = (
            "Your study statistics:\n"
            f"Total actions: {stats['total_actions']}\n"
            f"Questions asked: {stats['ask_count']}\n"
            f"Quizzes created: {stats['quiz_count']}\n"
            f"Notes saved: {stats['note_count']}\n"
            f"Active score: {stats['active_score']}"
        )
        await update.message.reply_text(message)
