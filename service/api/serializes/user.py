from marshmallow import Schema, fields, post_load, ValidationError, EXCLUDE, pre_load


class GroupSchema(Schema):
    name = fields.Str(required=True)
