from datetime import datetime
from typing import Any

from pydantic import BaseModel
from pydantic import model_validator


class HitEntityModel(BaseModel):
    title: str
    url: str
    created_at: datetime
    created_at_i: int
    objectID: int
    points: int
    story_id: int
    updated_at: datetime

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: dict[str, Any]) -> dict[str, Any]:
        data.pop("_highlightResult")
        data.pop("_tags")
        data.pop("author")
        data.pop("children")
        data.pop("num_comments")
        return data

    def to_text(self) -> str:
        return (
            f"title: {self.title} \n"
            f"url: {self.url} \n"
            f"created_at: {self.created_at.strftime('%Y/%m/%d %H:%M(UTC)')} \n"
        )


class HitModel(BaseModel):
    hits: list[HitEntityModel]

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: dict[str, Any]) -> dict[str, Any]:
        data.pop("exhaustive")
        data.pop("exhaustiveNbHits")
        data.pop("exhaustiveTypo")
        data.pop("hitsPerPage")
        data.pop("nbHits")
        data.pop("nbPages")
        data.pop("page")
        data.pop("params")
        data.pop("processingTimeMS")
        data.pop("processingTimingsMS")
        data.pop("query")
        data.pop("serverTimeMS", None)  # optional
        return data

    def has_result(self) -> bool:
        return len(self.hits) > 0
