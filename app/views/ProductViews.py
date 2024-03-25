from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.ProductSchemas import ProductResponseSchemas, ProductBaseSchemas, ProductUpdateSchemas
from app.models.ProductModels import ProductModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("products", __name__, description =
                """Product management endpoint"""
                )


@blp.route('/products')
class ProductsViews(MethodView):
    @blp.arguments(ProductBaseSchemas)
    @blp.response(201, ProductResponseSchemas)
    def post(self, product_data):
        """insert new product in shop account"""
        name = product_data["name"]
        price = product_data["price"]
        stock = product_data["stock"]
        description = product_data["description"]

        insert_new_product = ProductModel(name=name, price=price, stock=stock, description=description)
        try:
            db.session.add(insert_new_product)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(e)
            abort(500, message ="An error occurred while inserting new product.")
        return insert_new_product

    @blp.response(200, ProductResponseSchemas(many=True))
    def get(self):
        """retrieve all products data"""
        get_products_data = ProductModel.query.all()
        return get_products_data


@blp.route('/products/<string:product_id>')
class ProductViews(MethodView):
    @blp.arguments(ProductUpdateSchemas)
    @blp.response(201, ProductResponseSchemas)
    def put(self, product_data, product_id):
        """Update product data by it's id"""
        name = product_data["name"]
        price = product_data["price"]
        stock = product_data["stock"]
        description = product_data["description"]
        update_product = ProductModel.query.get_or_404(product_id)
        try:
            update_product.name = name
            update_product.price = price
            update_product.stock = stock
            update_product.description = description
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, message="An error occured while updating product data")
        return update_product

    @blp.response(200, ProductResponseSchemas)
    def get(self, product_id):
        """retrieve product data by it's id"""
        get_product_by_id = ProductModel.query.get(product_id)
        return get_product_by_id
    
    def delete(self, product_id):
        """delete product by it's id"""
        delete_product_by_id = ProductModel.query.get_or_404(product_id)
        db.session.delete(delete_product_by_id)
        db.session.commit()
        return {"message" : "Product deleted."}
