from marshmallow import Schema, fields


class UserResponseSchemas(Schema):
    id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class UserBaseSchemas(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()

class UserUpdateSchemas(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    address = fields.Str()

class UserLoginSchemas(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()