from src.database.connection import PostgresqlDatabase
from src.database.models.reservations import ReservationsModel

from datetime import datetime

from peewee import DoesNotExist

class ReservationsRepository:
    def __init__(self, db: PostgresqlDatabase):
        self.db = db
        self.model = ReservationsModel

    def get_reservations(self):
        result = self.model.select(
            self.model.id,
            self.model.destination,
            self.model.scheduled_at,
            self.model.created_at,
            self.model.updated_at
        ).dicts()
        return result

    def create_reservation(self, reservation: dict):
        result = self.model.create(**reservation)

        return result        

    def get_reservation(self, reservation_id: int):
        try:
            result = self.model.select(
                self.model.id,
                self.model.destination,
                self.model.scheduled_at,
                self.model.created_at,
                self.model.updated_at
            ).where(self.model.id == reservation_id).dicts().get()
        except DoesNotExist as e:
            return None
        return result

    def update_reservation(self, reservation_id: int, reservation):
        result = self.model.update(
            **{"updated_at": datetime.now().isoformat(timespec="minutes"), **reservation}
        ).where(self.model.id == reservation_id).execute()
        return result
    
    def delete_reservation(self, reservation_id: int):
        result = self.model.delete().where(self.model.id == reservation_id).execute()
        return result