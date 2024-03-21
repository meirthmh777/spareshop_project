# spareshop_project

I want to learn backend here using spareshop_project

## documentation day by day

### Day 1 March 18th, 2024

1. set up new app module `poetry new app`

2. set up environment `poetry add python-dotenv`
3. set up flask `poetry add flask`
4. create ./app/utils/db.py and mysql_connector.py modules to connect with database:
   - add Flask-SQLAlchemy `poetry add Flask-SQLAlchemy`
5. create buyer and shop models
6. add UUID (Universally Unique Identifiers) `poetry add uuid`
7. add passlib for hasing password `poetry add passlib`

### Day 2 March 19th, 2024

1. set up password in buyer and shop account model.
2. create buyer and shop account schemas:
   - using masrhmallow for shemas. marshmallow schemas can be used to: Validate input data. Deserialize input data to app-level objects. https://marshmallow.readthedocs.io/en/stable/ `poetry add marshmallow`
3. create buyer account view post method
   - using flask-smorest `poetry add flask-smorest` as database-agnostic framework library for creating REST APIs.
4. read https://flask-smorest.readthedocs.io/en/latest/openapi.html
5. install `poetry add mysql-connector-python`
6. countering with some errors. turned out it was UUID that required String datatype in model and schemas. Also change the column id from INT to VARCHAR(100) datatype.
7. do migrations. don't forget to import Migrate from flask_migrate in **init**.py:
   - `poetry add Flask-Migrate`
   - `poetry run flask db init`
   - `poetry run flask db migrate -m "try migration"`
   - `poetry run flask db upgrade`

### Day 3 March 20th, 2024

1. Create get, put and delete methods in userview query by it's id
2. using jwt to secure data
   - `poetry add Flask-JWT-Extended`

### Day 4 March 21th, 2024

1. create foreign key in shop.user_id table references to user.id
2. CONCEPT IS:
   - one user can have one shop account, that is why one user_id in shop table references to id in user table.
3. create post method in shop view that registered user creating new shop account with foreign key in shop.user_id references to user.id
4. correcting some errors like missing 1 argument and "Could not initialize target column for ForeignKey 'user.user_id' on table 'shop': table 'user' has no column named 'user_id'"

### How to run this project

1. create virtual environment : cntrl+shift+p, >Python: Create Environment, venv, create venv based on recommendation. or use `poetry config virtualenvs.in-project true`
2. set up virtual environment: `poetry shell`
3. install all dependencies : `poetry install`
4. run this project : `poetry run flask run`

### ~ GOD ALWAYS PROVIDES, HE'S ROOTING FOR YOU.
