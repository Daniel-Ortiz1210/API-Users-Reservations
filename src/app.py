from fastapi import FastAPI

from src.api.router import router
from src.database.connection import DatabaseConnection
from src.database.models.reservations import ReservationsModel

app: FastAPI = FastAPI(
    title='API',
    description='',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json',
)

@app.on_event('startup')
async def startup_event():
    database = DatabaseConnection().get_db()
    database.create_tables([ReservationsModel])

app.include_router(router)
