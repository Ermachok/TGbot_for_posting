import os

from dotenv import load_dotenv
from handlers import (invalid_input_handler, post_detail_handler,
                      posts_handler, start_handler)
from middlewares import setup_logging
from states import BotStates
from telegram.ext import (ApplicationBuilder, CallbackQueryHandler,
                          CommandHandler, ConversationHandler, MessageHandler,
                          filters)

load_dotenv()
setup_logging()


def main():
    token = os.getenv("TELEGRAM_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_handler))

    post_conv = ConversationHandler(
        entry_points=[CommandHandler("posts", posts_handler)],
        states={
            BotStates.POST_CHOICE: [
                CallbackQueryHandler(post_detail_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, invalid_input_handler),
            ],
        },
        fallbacks=[],
    )

    app.add_handler(post_conv)

    app.run_polling()


main()
