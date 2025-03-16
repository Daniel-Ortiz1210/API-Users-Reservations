from fastapi import APIRouter, Depends, HTTPException, status, Path
from fastapi.responses import JSONResponse

from src.utils.logger import Logger

router = APIRouter(
    prefix='/reservations',
    tags=['Reservations']
    )

@router.get('/')
async def get_reservations():
    
    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations] [GET] Get all reservations")
    
    return []

@router.post('/')
async def create_reservation():

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations] [POST] Create reservation")

    return {}

@router.get('/{reservation_id}')
async def get_reservation(reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to get', gt=0)):

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [POST] Get reservation with ID {reservation_id}")


    return {}

@router.put('/{reservation_id}')
async def update_reservation(reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to update', gt=0)):

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [PUT] Update reservation with ID {reservation_id}")
    
    return {}

@router.delete('/{reservation_id}')
async def delete_reservation(reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to delete', gt=0)):
    
    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [DELETE] Delete reservation with ID {reservation_id}")
    
    return {}
