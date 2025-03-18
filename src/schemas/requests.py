from pydantic import BaseModel, field_validator, Field
from datetime import datetime
from typing import List, Optional, Dict, Union


class ReservationRequestSchema(BaseModel):
    scheduled_at: str = Field(datetime.now().isoformat(timespec='minutes'), title="Date of reservation", description="The date of the reservation in the format YYYY-MM-DD")
    destination: str = Field(..., title="Destination", description="The destination of the reservation")


class PassengerIdRequestSchema(BaseModel):
    passenger_id: int = Field(..., title="Passenger ID", description="The ID of the passenger to associate with the reservation")
    