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

    POINTS_THRESHOLD: int = 500
    CREATED_AT_THRESHOLD_SEC: int = 12 * 60 * 60  # 1 day

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
                    value=self.POINTS_THRESHOLD,
                ),
                HackerNewsNumericFilter(
                    key=HackerNewsNumericFiltersKey.CREATED_AT_I,
                    condition=">=",
                    value=self.current_timestamp_sec() - self.CREATED_AT_THRESHOLD_SEC,
                ),
            ],
            bypass_cache=bypass_cache,
        )
