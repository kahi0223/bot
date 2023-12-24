from typing import Any

from pydantic import BaseModel
from pydantic import model_validator


class GetMeResultModel(BaseModel):
    id_: int
    is_bot: bool
    first_name: str
    username: str
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate_id(cls, data: dict[str, Any]) -> dict[str, Any]:
        data["id_"] = data["id"]
        data.pop("id")
        return data
