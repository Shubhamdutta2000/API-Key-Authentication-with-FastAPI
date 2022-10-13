# API Key Authentication with FastAPI

> This is authentication in the form of an arbitrary string of any length that allows access to an API.

## Feature:

- DB Connection Configuration with PostgresSQL and store all db creds in .env file and load it from seperate EnvConfig file.
- API Key Authentication for:
  - Checking for a query parameter containing the API key
  - Checking for a header containing the API key
  - Checking for a cookie containing the API key
- GET Endpoint to expose all data with proper Pagination (of particular page and limit)
- When no query parameter is specified in the api, the page and limit are set by default which are stored in .env file.

<br />

## References:

- https://nilsdebruin.medium.com/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680
