from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.ShopAccountSchemas import ShopResponseSchemas, ShopBaseSchemas, ShopUpdateSchemas
from app.models.ShopAccountModel import ShopModel
from app.utils.db import db



blp = Blueprint('shops', __name__, description=
                """shop account management endpoint"""
                )

@blp.route('/shops')
class ShopsViews(MethodView):
    @blp.arguments(ShopBaseSchemas)
    @blp.response(201, ShopResponseSchemas)
    def post(sel, shop_data):
        """registered user create new shop"""
        user_id = shop_data["user_id"]
        shopname = shop_data["shopname"]
        email = shop_data["email"]
        password = shop_data["password"]
        address = shop_data["address"]
        if ShopModel.query.filter_by(shopname=shopname).first():
            abort(400, message="shop name already exists. Try another shop name")
        if ShopModel.query.filter_by(email=email).first():
            abort(400, message="email already registered. Try another email!")
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
        
    @blp.response(200, ShopResponseSchemas(many=True))
    def get(self):
        """retrieve all shop data"""
        get_all_shops_data = ShopModel.query.all()
        print(get_all_shops_data)
        return get_all_shops_data

@blp.route('/shops/<string:shop_id>')
class ShopView(MethodView):
    @blp.response(200, ShopResponseSchemas)
    def get(self, shop_id):
        """retrieve shop data by it's id"""
        get_shop_by_id = ShopModel.query.get(shop_id)
        return get_shop_by_id
    
    @blp.arguments(ShopUpdateSchemas)
    @blp.response(201, ShopResponseSchemas)
    def put(self, shop_data, shop_id):
        """update shop data by it's id"""
        shopname = shop_data['shopname']
        email = shop_data['email']
        password = shop_data['password'] 
        address = shop_data['address']
        update_shop = ShopModel.query.get_or_404(shop_id)
        if ShopModel.query.filter_by(shopname=shopname).first():
            abort(400, message="Shop name already exists. Try another shop name")
        if ShopModel.query.filter_by(email=email).first():
            abort(400, message="email already used. Try another email!")
        try:
            update_shop.shopname = shopname
            update_shop.email = email
            update_shop.address = address
            update_shop.set_password(password)
            db.session.commit()
        except Exception as e:
            print(e)
            abort(500, message="An error occured while updating shop data")
        return update_shop
    
    def delete(self, shop_id):
        """delete shop by it's id"""
        delete_shop_account = ShopModel.query.get(shop_id)
        db.session.delete(delete_shop_account)
        db.session.commit()
        return{"message" : "Shop account is deleted!"}

