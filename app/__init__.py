from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


from app.utils.db import db
from app.utils.mysql_connector import my_sql_string
from app.views.UserAccountViews import blp as UserAccountView
from app.views.ShopAccountViews import blp as ShopAccountView
from app.views.ProductViews import blp as ProductView
from app.views.LoginView import blp as LoginView



load_dotenv()

app = Flask(__name__)
app.config["API_TITLE"] = "SPARESHOP RESTful API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = my_sql_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_SECRET_KEY"] = "secret key random string"


db.init_app(app)
with app.app_context():
    db.create_all()
api = Api(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# register blueprints
api.register_blueprint(UserAccountView)
api.register_blueprint(ShopAccountView)
api.register_blueprint(ProductView)
api.register_blueprint(LoginView)


@app.route('/')
def hello_universe():
    return "hello universe"