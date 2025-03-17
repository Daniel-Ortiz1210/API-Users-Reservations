from fastapi import APIRouter, Depends, HTTPException, status, Path, Body
from fastapi.responses import JSONResponse, Response

from src.utils.logger import Logger
from src.schemas.requests import ReservationRequestSchema
from src.schemas.responses import SuccessResponse, BadResponse
from src.database.repository.reservations import ReservationsRepository
from src.database.connection import DatabaseConnection

router = APIRouter(
    prefix='/reservations',
    tags=['Reservations']
    )


@router.get('/')
async def get_reservations():
    
    logger = Logger()
    
    logger.log('INFO', f"[/api/v1/reservations] [GET] Get all reservations")

    db = DatabaseConnection()
    
    repository = ReservationsRepository(db)
    
    reservations = repository.get_reservations()

    json_response = SuccessResponse(data=reservations).model_dump()

    db.close()

    return JSONResponse(content=json_response, status_code=status.HTTP_200_OK)


@router.post('/')
async def create_reservation(
    request_body: dict = Body(..., json_schema_extra=ReservationRequestSchema.model_json_schema())
):

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations] [POST] Create reservation")

    try:
        request_body = ReservationRequestSchema(**request_body)
    except ValueError as e:
        logger.log('ERROR', f"[/api/v1/reservations] [POST] {str(e)}")
        json_bad_response = BadResponse(detail={}).model_dump()
        return JSONResponse(content=json_bad_response, status_code=status.HTTP_400_BAD_REQUEST)
    
    request_body_to_dict = request_body.model_dump()
    
    # Query the database to create the reservation
    db = DatabaseConnection()

    repository = ReservationsRepository(db)

    repository.create_reservation(request_body_to_dict)

    db.close()
    
    json_response = SuccessResponse(data=request_body_to_dict).model_dump()

    return JSONResponse(content=json_response, status_code=status.HTTP_201_CREATED)


@router.get('/{reservation_id}')
async def get_reservation(reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to get', gt=0)):

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [POST] Get reservation with ID {reservation_id}")

    # Query the database to get the reservation with the ID
    db = DatabaseConnection()

    repository = ReservationsRepository(db)

    reservation = repository.get_reservation(reservation_id)

    if not reservation:
        logger.log('ERROR', f"[/api/v1/reservations/{reservation_id}] [POST] Reservation with ID {reservation_id} not found")
        json_bad_response = BadResponse(detail={"reservation": "Not found"}).model_dump()
        return JSONResponse(content=json_bad_response, status_code=status.HTTP_404_NOT_FOUND)
    
    json_response = SuccessResponse(data=reservation).model_dump()

    db.close()

    return JSONResponse(content=json_response, status_code=status.HTTP_200_OK)


@router.put('/{reservation_id}')
async def update_reservation(
    reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to update', gt=0),
    request_body: dict = Body(..., json_schema_extra=ReservationRequestSchema.model_json_schema())
    ):

    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [PUT] Update reservation with ID {reservation_id}")

    try:
        # Validate the request body
        request_body = ReservationRequestSchema(**request_body)
    except ValueError as e:
        logger.log('ERROR', f"[/api/v1/reservations/{reservation_id}] [PUT] {str(e)}")
        json_bad_response = BadResponse(message="Validation Error").model_dump()
        return JSONResponse(content=json_bad_response, status_code=status.HTTP_400_BAD_REQUEST)
    
    request_body_to_dict = request_body.model_dump()

    # Query the database to update the reservation with the ID

    db = DatabaseConnection()

    repository = ReservationsRepository(db)

    reservation = repository.get_reservation(reservation_id)

    if not reservation:
        logger.log('ERROR', f"[/api/v1/reservations/{reservation_id}] [PUT] Reservation with ID {reservation_id} not found")
        json_bad_response = BadResponse(message="Reservation Not Found").model_dump()
        return JSONResponse(content=json_bad_response, status_code=status.HTTP_404_NOT_FOUND)

    repository.update_reservation(reservation_id, request_body_to_dict)

    json_response = SuccessResponse(data=request_body_to_dict).model_dump()

    db.close()

    return JSONResponse(content=json_response, status_code=status.HTTP_200_OK)


@router.delete('/{reservation_id}')
async def delete_reservation(reservation_id: int = Path(..., title='Reservation ID', description='The ID of the reservation to delete', gt=0)):
    
    logger = Logger()
    logger.log('INFO', f"[/api/v1/reservations/{reservation_id}] [DELETE] Delete reservation with ID {reservation_id}")
    
    # Query the database to delete the reservation with the ID
    db = DatabaseConnection()

    repository = ReservationsRepository(db)

    reservation = repository.get_reservation(reservation_id)

    if not reservation:
        logger.log('ERROR', f"[/api/v1/reservations/{reservation_id}] [DELETE] Reservation with ID {reservation_id} not found")
        json_bad_response = BadResponse(message="Reservation Not Found").model_dump()
        return JSONResponse(content=json_bad_response, status_code=status.HTTP_404_NOT_FOUND)

    repository.delete_reservation(reservation_id)

    db.close()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

