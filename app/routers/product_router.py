from typing import Union

from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey

from app.crud.product_crud import list_all_product
from app.dependencies import get_api_key
from app.utils.conv import conv
from app.config.EnvConfig import get_env_config, EnvConfig

env_config: EnvConfig = get_env_config()

router = APIRouter(prefix="/v1/api/product", tags=["Product"])


@router.get("/", response_model_exclude_none=True)
def get_data(api_key: APIKey = Depends(get_api_key), limit: Union[str, None] = env_config.default_limit, page: Union[str, None] = env_config.default_page):
    """
       - GET Endpoint to expose data with Pagination
        Args:
           api_key (APIKey): Defaults to Depends(get_api_key).
           limit (Union[str, None] = None): Query Param for specific limit of data in particular page with default value
           page (Union[str, None] = None): Query Param for particular no. of page with default value
        Returns:
           list of all drugs in json format
    """
    response = list_all_product(limit, page)
    # df = conv(response)
    # return df
    return response
