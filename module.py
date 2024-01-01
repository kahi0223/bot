from injector import Module
from injector import provider

from bot import Bot
from news import News


class AppModule(Module):
    @provider
    def provide_bot(self) -> Bot:
        return Bot()

    @provider
    def provide_news(self) -> News:
        return News()
