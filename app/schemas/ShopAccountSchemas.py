from marshmallow import Schema, fields


class ShopResponseSchemas(Schema):
    id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()