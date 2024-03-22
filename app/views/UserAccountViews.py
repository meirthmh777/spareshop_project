from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.schemas.UserAccountSchemas import UserResponseSchemas, UserBaseSchemas, UserUpdateSchemas
from app.models.UserAccountModel import UserModel
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError
# from flask_jwt_extended import jwt_required

blp = Blueprint("users", __name__, description=
                """user account management endpoint"""
                )

@blp.route('/users')
class UsersView(MethodView):
    @blp.arguments(UserBaseSchemas)
    @blp.response(201, UserResponseSchemas)
    def post(self, user_data):
        """create new user account"""
        username = user_data['username']
        email = user_data['email']
        password = user_data['password']
        address = user_data['address']
        if UserModel.query.filter_by(username=username).first():
            abort(400, message="Username already exists. Try another username!")
        if UserModel.query.filter_by(email=email).first():
            abort(400, message="Email already registered. Try another email!")
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
    
    @blp.response(200, UserResponseSchemas(many=True))
    def get(self):
        """retrieve users data"""
        get_all_users_data = UserModel.query.all()
        return get_all_users_data

@blp.route('/users/<string:user_id>')
class UserView(MethodView):
    # @jwt_required
    @blp.response(200, UserResponseSchemas)
    def get(self, user_id):
        """retrieve user data by it's id"""
        get_user_by_id = UserModel.query.get(user_id)
        return get_user_by_id

    # @jwt_required
    @blp.arguments(UserUpdateSchemas)
    @blp.response(201, UserResponseSchemas)
    def put(self, user_data, user_id):
        """update user data by it's id"""
        username = user_data['username']
        email = user_data['email']
        password = user_data['password']
        address = user_data['address']
        update_user = UserModel.query.get_or_404(user_id)
        if UserModel.query.filter_by(username=username).first():
            abort(400, message="Username already exists. Try another username!")
        if UserModel.query.filter_by(email=email).first():
            abort(400, message="Email already used. Try another email!")
        try:
            update_user.username = username
            update_user.email = email
            update_user.address = address
            update_user.set_password(password)
            db.session.commit()
        except Exception as e:
            print(e)
            abort(500, message="An error occured while updating user data")
        return update_user
    
    # @jwt_required
    def delete(self, user_id):
        """delete user by it's id"""
        delete_user_account = UserModel.query.get_or_404(user_id)
        db.session.delete(delete_user_account)
        db.session.commit()
        return{"message" : "User account is deleted!"}