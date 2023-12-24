from pydantic import BaseModel
from pydantic import model_validator


class UserModel(BaseModel):
    id_: int
    is_bot: bool
    first_name: str
    lats_name: str | None = None
    username: str | None = None
    language_code: str | None = None

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def validate_id(cls, data: dict[str, int]) -> dict[str, int]:
        data["id_"] = data["id"]
        data.pop("id")
        return data
