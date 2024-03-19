from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv
from flask_migrate import Migrate

from app.utils.db import db
from app.utils.mysql_connector import my_sql_string
from app.views.UserAccountViews import blp as UserAccountView



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


db.init_app(app)
with app.app_context():
    db.create_all()
api = Api(app)
migrate = Migrate(app, db)

# register blueprints
api.register_blueprint(UserAccountView)


@app.route('/')
def hello_universe():
    return "hello universe"