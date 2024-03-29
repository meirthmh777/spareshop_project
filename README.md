# spareshop_project

I want to learn backend here using spareshop_project

## documentation day by day

### Day 1 Monday March 18th, 2024

1. set up new app module `poetry new app`

2. set up environment `poetry add python-dotenv`
3. set up flask `poetry add flask`
4. create ./app/utils/db.py and mysql_connector.py modules to connect with database:
   - add Flask-SQLAlchemy `poetry add Flask-SQLAlchemy`
5. create user and shop models
6. add UUID (Universally Unique Identifiers) `poetry add uuid`
7. add passlib for hasing password `poetry add passlib`

### Day 2 Tuesday March 19th, 2024

1. set up password in user and shop account model.
2. create user and shop account schemas:
   - using masrhmallow for shemas. marshmallow schemas can be used to: Validate input data. Deserialize input data to app-level objects. https://marshmallow.readthedocs.io/en/stable/ `poetry add marshmallow`
3. create user account view post method
   - using flask-smorest `poetry add flask-smorest` as database-agnostic framework library for creating REST APIs.
4. read https://flask-smorest.readthedocs.io/en/latest/openapi.html
5. install `poetry add mysql-connector-python`
6. countering with some errors. turned out it was UUID that required String datatype in model and schemas. Also change the column id from INT to VARCHAR(100) datatype.
7. do migrations. don't forget to import Migrate from flask_migrate in **init**.py:
   - `poetry add Flask-Migrate`
   - `poetry run flask db init`
   - `poetry run flask db migrate -m "try migration"`
   - `poetry run flask db upgrade`

### Day 3 Wednesday March 20th, 2024

1. Create get, put and delete methods in userview query by it's id
2. using jwt to secure data
   - `poetry add Flask-JWT-Extended`

### Day 4 Thursday March 21th, 2024

1. create foreign key in shop.user_id table references to user.id
2. CONCEPT IS:
   - one user can have one shop account, that is why one user_id in shop table references to id in user table.
3. create post method in shop view that registered user creating new shop account with foreign key in shop.user_id references to user.id
4. correcting some errors like missing 1 argument and "Could not initialize target column for ForeignKey 'user.user_id' on table 'shop': table 'user' has no column named 'user_id'"

### Day 5 Friday March 22th, 2024

1. create get method to retrieve all shops. encounter error where thunder clinet response with empty object {}. turns out bcs of my response schema doesn't have argument many=True.
2. encountering error 'dict' object has no attribute 'address' it occurs when shop_data.address = address it should be update_shop_data.address = address
3. TypeError: int() argument must be a string, a bytes-like object or a real number, not 'SchemaMeta' ini kalau kurang response ny 201
4. create other methods like get, put and delete shop account by it's id.

### Day 6 Monday March 25th, 2024

1. create product table
2. create transaction_type table
3. create transaction table which has so many foreign key yeeahh
4. create POST and GET productsview for '/products' route and PUT, GET, DELETE in '/products/<string:product_id>' route. encountering some errors:
   - get_all_products = ProductModel.query.get(all) it must be query.all()
   - SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 9-10: truncated \UXXXXXXXX escape turns out it cannot generate comment lines in certain positions

### Day 7 Tuesday March 26th, 2024

1. create LoginView.py and make sure all of endpoints with @jwt_required work in userview.py.
2. RuntimeError: You must initialize a JWTManager with this flask application before using this method. I should Initialize JWTManager in init.py
3. RuntimeError: JWT_SECRET_KEY or flask SECRET_KEY must be set when using symmetric algorithm "HS256". I should initialize app.config["JWT_SECRET_KEY"] = "secret key random string" in init.py
4. hit the login route in thunder client then boom I got the access token.
5. TypeError: jwt_required.<locals>.wrapper() got an unexpected keyword argument 'user_id' turns out I use @jwt_required is a call back so it should be @jwt_required(). like @jwt_required() with () it will pass the arguments to the decorator.

### How to run this project

1. create virtual environment : cntrl+shift+p, >Python: Create Environment, venv, create venv based on recommendation. or use `poetry config virtualenvs.in-project true`
2. set up virtual environment: `poetry shell`
3. install all dependencies : `poetry install`
4. run this project : `poetry run flask run`

### ~ GOD ALWAYS PROVIDES, HE'S ROOTING FOR YOU.

#### another day, another error, another slay!
