from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def posts_keyboard(posts: list) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(post["title"], callback_data=str(post["id"]))]
        for post in posts
    ]
    return InlineKeyboardMarkup(buttons)
