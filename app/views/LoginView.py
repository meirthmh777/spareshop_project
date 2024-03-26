from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.models.UserAccountModel import UserModel
from app.schemas.UserAccountSchemas import UserLoginSchemas
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from datetime import timedelta
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint('/login', __name__, description = 
                """Login endpoint management"""
                )


@blp.route('/login')
class LoginView(MethodView):
    @blp.arguments(UserLoginSchemas)
    def post(self, user_data):
        """User login"""
        print(user_data)
        try:
            match_user:UserModel = UserModel.query.filter(UserModel.email == user_data["email"]).first()
            if match_user == None:
                abort(HTTPStatus.CONFLICT, message = "User email not found")
            if match_user.check_password(user_data["password"]) == False:
                abort(HTTPStatus.CONFLICT, message = "Wrong password")
            access_token = create_access_token(identity=match_user.id, fresh=True, expires_delta=timedelta(days=7))
            return{"access token" : access_token}
        
        except SQLAlchemyError as e:
            print(e)
            abort(HTTPStatus.CONFLICT, message = "Failed to login")