from pydantic import BaseModel
from pydantic import model_validator

from .chat import ChatModel
from .user import UserModel


class SendMessageResultModel(BaseModel):
    message_id: int
    from_: UserModel
    chat: ChatModel
    date: int
    text: str

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate_from(cls, data: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
        data["from_"] = data["from"]
        data.pop("from")
        return data

