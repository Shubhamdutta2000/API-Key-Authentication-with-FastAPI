from app.config.EnvConfig import get_env_config
import psycopg2 as db_connect

config = get_env_config()


def connect_db():
    try:
        host_name = config.host_name
        db_user = config.db_user
        db_password = config.db_password
        db_name = config.db_name
        connection = db_connect.connect(host=host_name, user=db_user, password=db_password, database=db_name)
        return connection
    except:
        print("Error connecting DB")
