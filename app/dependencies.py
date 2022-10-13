from fastapi import HTTPException, status, Security
from fastapi.security.api_key import APIKeyHeader, APIKeyQuery, APIKeyCookie
from app.config.EnvConfig import get_env_config, EnvConfig

env_config: EnvConfig = get_env_config()


api_key_header = APIKeyHeader(name=env_config.api_key_name, auto_error=False)
api_key_query = APIKeyQuery(name=env_config.api_key_name, auto_error=False)
api_key_cookie = APIKeyCookie(name=env_config.api_key_name, auto_error=False)

async def get_api_key(
    api_key_header_data: str = Security(api_key_header),
    api_key_query_data: str = Security(api_key_query),
    api_key_cookie_data: str = Security(api_key_cookie),
):
    """
       - Checking for a header containing the API key
        Args:
           api_key_header_data (str): Defaults to Security(api_key_header)
           api_key_query_data (str): Defaults to Security(api_key_query)
           api_key_cookie_data (str): Defaults to Security(api_key_cookie)
        Returns:
            api key value
    """
    if api_key_header_data == env_config.api_key:
        return api_key_header_data
    elif api_key_query_data == env_config.api_key:
        return api_key_query_data
    elif api_key_cookie_data == env_config.api_key:
        return api_key_cookie_data
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
