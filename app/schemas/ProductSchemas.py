from marshmallow import Schema, fields


class ProductResponseSchemas(Schema):
    id = fields.Str()
    name = fields.Str()
    price = fields.Float()
    stock = fields.Integer()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

class ProductBaseSchemas(Schema):
    name = fields.Str()
    price = fields.Float()
    stock = fields.Integer()
    description = fields.Str()


class ProductUpdateSchemas(Schema):
    name = fields.Str()
    price = fields.Float()
    stock = fields.Integer()
    description = fields.Str()







