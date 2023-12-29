from telegram_handler import TelegramHandler


class Bot:
    def __init__(self) -> None:
        self.telegram = TelegramHandler()

    def group_chat_id(self) -> int | None:
        return self.telegram.group_chat_id

    def is_active(self) -> bool:
        try:
            self.telegram.get_me()
            return True
        except Exception as e:
            print(e)
            return False

    def send_message(self, chat_id: int, text: str) -> None:
        self.telegram.send_message(chat_id=chat_id, text=text)

    def get_first_group_chat_id(self) -> int | None:
        group = self.telegram.get_updates()
        if len(group.root) == 0:
            return None
        return group.root[0].my_chat_member.chat.id_
