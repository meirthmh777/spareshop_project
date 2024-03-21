from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.ShopAccountSchemas import ShopResponseSchemas, ShopBaseSchemas
from app.models.ShopAccountModel import ShopModel
from app.utils.db import db



blp = Blueprint('/shop', __name__, description=
                """"shop account management endpoint"""
                )

@blp.route('/shop')
class ShopViews(MethodView):
    @blp.arguments(ShopBaseSchemas)
    @blp.response(201, ShopResponseSchemas)
    def post(sel, item_data):
        """registered user create new shop"""
        user_id = item_data["user_id"]
        shopname = item_data["shopname"]
        email = item_data["email"]
        password = item_data["password"]
        address = item_data["address"]
        if ShopModel.query.filter_by(shopname=shopname).first():
            abort(400, message="shop name already exists.")
        user_register_new_shop = ShopModel(user_id=user_id, shopname=shopname, email=email, password=password, address=address)
        user_register_new_shop.set_password(password)
        try:
            db.session.add(user_register_new_shop)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            abort(500, message="An error occured while register new shop")
        return user_register_new_shop
        


