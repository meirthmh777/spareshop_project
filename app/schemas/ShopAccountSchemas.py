from marshmallow import Schema, fields


class ShopResponseSchemas(Schema):
    id = fields.Str()
    user_id = fields.Str()
    shopname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class ShopBaseSchemas(Schema):
    user_id = fields.Str()
    shopname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()

class ShopUpdateSchemas(Schema):
    shopname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()