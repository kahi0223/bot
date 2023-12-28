from bot import Bot


if __name__ == "__main__":
    bot = Bot()
    if bot.is_active():
        bot.send_message(
            chat_id=bot.get_first_group_chat_id(),
            text="Hello, World!",
        )
    else:
        print("Bot is not active.")
