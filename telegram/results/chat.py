from pydantic import BaseModel
from pydantic import model_validator


class ChatModel(BaseModel):
    id_: int
    title: str
    type: str
    all_members_are_administrators: bool

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate_id(cls, data: dict[str, int]) -> dict[str, int]:
        data["id_"] = data["id"]
        data.pop("id")
        return data
