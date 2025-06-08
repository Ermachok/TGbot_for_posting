from api import get_post, get_posts
from keyboards import posts_keyboard
from states import BotStates
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Нажми /posts чтобы посмотреть посты.")


async def posts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    posts = get_posts()
    await update.message.reply_text("Выбери пост:", reply_markup=posts_keyboard(posts))
    return BotStates.POST_CHOICE


async def post_detail_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    post_id = int(query.data)
    post = get_post(post_id)
    await query.edit_message_text(
        f"*{post['title']}*\n\n{post['content']}\n{post['created_at']}",
        parse_mode="Markdown",
    )

    return ConversationHandler.END


async def invalid_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Пожалуйста, выбери пост, используя кнопки выше"
    )
    return BotStates.POST_CHOICE
