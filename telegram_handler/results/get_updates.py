from typing import Any

from pydantic import BaseModel
from pydantic import RootModel
from pydantic import model_validator

from .user import UserModel


class GetUpdateResultEntityMyChatMemberChatModel(BaseModel):
    id_: int  # chat id for group
    title: str
    type: str
    all_members_are_administrators: bool

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def id_(cls, data: dict[str, Any]) -> dict[str, Any]:
        data['id_'] = data['id']
        del data['id']
        return data


class GetUpdateResultEntityMyChatMemberModel(BaseModel):
    chat: GetUpdateResultEntityMyChatMemberChatModel
    from_: UserModel

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def pop(cls, data: dict[str, Any]) -> dict[str, Any]:
        # remove unused fields
        data.pop('old_chat_member')
        data.pop('new_chat_member')
        # data.pop('from')
        data.pop('date')
        return data

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def from_(cls, data: dict[str, Any]) -> dict[str, Any]:
        data['from_'] = data['from']
        del data['from']
        return data


class GetUpdatesResultEntityModel(BaseModel):
    update_id: int
    my_chat_member: GetUpdateResultEntityMyChatMemberModel


class GetUpdatesResultModel(RootModel):
    root: list[GetUpdatesResultEntityModel]
