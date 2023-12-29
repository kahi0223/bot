from bot import Bot
from news import News

if __name__ == "__main__":
    news = News()
    hot_news = news.hot_news(bypass_cache=True)
    if not hot_news.has_result():
        print("No result.")
        exit(0)

    bot = Bot()
    group_chat_id = bot.group_chat_id()
    if group_chat_id is None:
        print("No group chat id.")
        exit(0)
    for hit in hot_news.hits:
        bot.send_message(chat_id=group_chat_id, text=hit.to_text())
