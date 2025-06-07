import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    CallbackQueryHandler, ConversationHandler
)
from handlers import start_handler, posts_handler, post_detail_handler
from middlewares import setup_logging
from states import POST_CHOICE

load_dotenv()
setup_logging()

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_handler))

    post_conv = ConversationHandler(
        entry_points=[CommandHandler("posts", posts_handler)],
        states={
            POST_CHOICE: [CallbackQueryHandler(post_detail_handler)],
        },
        fallbacks=[]
    )

    app.add_handler(post_conv)

    app.run_polling()

main()