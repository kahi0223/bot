from time import time
from dataclasses import dataclass


from hacker_news import HackerNews
from hacker_news import HackerNewsNumericFilter
from hacker_news import HackerNewsNumericFiltersKey
from hacker_news import HackerNewsTag
from hacker_news import HitModel


@dataclass
class News:
    hacker_news = HackerNews()

    cache_expire_sec: int = 60 * 60  # 1 hour
    points_threshold: int = 500
    created_at_threshold_sec: int = 12 * 60 * 60  # 12 hours

    @staticmethod
    def current_timestamp_sec() -> int:
        return int(time())

    def hot_news(self, bypass_cache: bool = False) -> HitModel:
        return self.hacker_news.search_by_date(
            tags=HackerNewsTag.STORY,
            numeric_filters=[
                HackerNewsNumericFilter(
                    key=HackerNewsNumericFiltersKey.POINTS,
                    condition=">=",
                    value=self.points_threshold,
                ),
                HackerNewsNumericFilter(
                    key=HackerNewsNumericFiltersKey.CREATED_AT_I,
                    condition=">=",
                    value=self.current_timestamp_sec() - self.created_at_threshold_sec,
                ),
            ],
            bypass_cache=bypass_cache,
            cache_expire_sec=self.cache_expire_sec,
        )
