from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.UserAccountSchemas import UserResponseSchemas, UserBaseSchemas, UserUpdateSchemas
from app.models.UserAccountModel import UserModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("user", __name__, description="""user account management endpoint""")

@blp.route('/user')
class UserView(MethodView):
    @blp.arguments(UserBaseSchemas)
    @blp.response(201, UserResponseSchemas)
    def post(self, item_data):
        """create new user account"""
        username = item_data['username']
        email = item_data['email']
        password = item_data['password']
        address = item_data['address']
        if UserModel.query.filter_by(username=username).first():
            abort(400, message="Username already exists")
        new_user_register = UserModel(username=username, email=email,password=password, address=address)
        new_user_register.set_password(password)
        try:
            db.session.add(new_user_register)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(e)
            abort(500, message="An error occurred while inserting new user.")
        return new_user_register
    



