from fastapi import FastAPI
from app.routers import product_router

app = FastAPI()

app.include_router(product_router.router)

@app.get("/")
def root():
    return {"message": "Hello User!"}
