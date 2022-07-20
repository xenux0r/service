from dataclasses import dataclass
from marshmallow import Schema, fields, post_load


@dataclass
class UserGroup:
    name: str


class UserGroupSchema(Schema):
    name = fields.Str(required=True)

    @post_load
    def convert(self, data, **kwargs):
        return UserGroup(**data)

