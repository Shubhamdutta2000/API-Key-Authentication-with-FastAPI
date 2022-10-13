import os
from dotenv import load_dotenv
load_dotenv()

class EnvConfig:
    host_name = os.environ.get("host_name")
    db_name = os.environ.get("db_name")
    db_password = os.environ.get("db_password")
    db_user = os.environ.get("db_user")
    table_name = os.environ.get("table_name")
    api_key = os.environ.get("api_key")
    api_key_name = os.environ.get("api_key_name")

def get_env_config():
    return EnvConfig()
