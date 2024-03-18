import os

username = os.getenv['DATABASE_USERNAME']
password = os.getenv['DATABASE_PASSWORD']
host_url = os.getenv['DATABASE_URL']
db_name = os.getenv['DATABASE_NAME']

print("connecting to MySQL Database")

my_sql_string = f"mysql+mysqlconnector://{username}:{password}@{host_url}/{db_name}"

print(f'Connected to the MySQL Database at {host_url}')