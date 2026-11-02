import logging
import os

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from handlers.resource_handlers import register_resource_handlers

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Build the welcome screen's inline menu."""
    keyboard = [
        [
            InlineKeyboardButton("📚 Study resources", callback_data="resources"),
            InlineKeyboardButton("📝 Quizzes", callback_data="quizzes"),
        ],
        [
            InlineKeyboardButton("👤 My account", callback_data="account"),
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Welcome a student and show the main menu."""
    user = update.effective_user
    name = user.first_name if user and user.first_name else "student"
    await update.effective_message.reply_text(
        f"Welcome, {name}, to Smart Revision Assistant!\n\n"
        "Choose an option below to get started.",
        reply_markup=main_menu_keyboard(),
    )


async def handle_menu_action(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Respond to selections from the inline menu."""
    query = update.callback_query
    if query is None:
        return

    await query.answer()
    messages = {
        "quizzes": (
            "📝 Quizzes\n\n"
            "Interactive revision quizzes are coming soon."
        ),
        "account": (
            "👤 My account\n\n"
            "Student profiles and progress tracking are coming soon."
        ),
        "about": (
            "ℹ️ About Smart Revision Assistant\n\n"
            "We help Kenyan secondary school students find revision "
            "resources and prepare for examinations."
        ),
    }
    message = messages.get(query.data)
    if message is None:
        await query.edit_message_text(
            "That menu option is not available. Please use /start to try again."
        )
        return

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🏠 Main menu", callback_data="home")]]
    )
    await query.edit_message_text(message, reply_markup=keyboard)


async def show_home(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Return to the main menu from a submenu."""
    query = update.callback_query
    if query is None:
        return

    await query.answer()
    user = update.effective_user
    name = user.first_name if user and user.first_name else "student"
    await query.edit_message_text(
        f"Welcome, {name}, to Smart Revision Assistant!\n\n"
        "Choose an option below to get started.",
        reply_markup=main_menu_keyboard(),
    )


def build_application(token: str) -> Application:
    """Create the Telegram application and register bot handlers."""
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(show_home, pattern="^home$"))
    register_resource_handlers(application)
    application.add_handler(
        CallbackQueryHandler(
            handle_menu_action,
            pattern="^(quizzes|account|about)$",
        )
    )
    return application


def main() -> None:
    token = (
        os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        or os.getenv("BOT_TOKEN", "").strip()
    )
    if not token:
        raise SystemExit(
            "Neither TELEGRAM_BOT_TOKEN nor BOT_TOKEN is set. Copy "
            ".env.example to .env and "
            "add your token from Telegram's BotFather."
        )

    application = build_application(token)
    logger.info("Starting Smart Revision Assistant bot")
    application.run_polling()


if __name__ == "__main__":
    main()
