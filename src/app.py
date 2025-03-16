from fastapi import FastAPI

from src.api.router import router

app: FastAPI = FastAPI(
    title='API',
    description='',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json',
)

app.include_router(router)
