from src.database.connection import PostgresqlDatabase
from src.database.models.reservations import ReservationsModel

from peewee import DoesNotExist

class ReservationsRepository:
    def __init__(self, db: PostgresqlDatabase):
        self.db = db
        self.model = ReservationsModel

    def get_reservations(self):
        result = self.model.select().dicts()
        return result

    def create_reservation(self, reservation: dict):
        result = self.model.create(**reservation)

        return result        

    def get_reservation(self, reservation_id: int):
        try:
            result = self.model.get_by_id(reservation_id).dicts()
        except DoesNotExist as e:
            return None
        return result

    def update_reservation(self, reservation_id: int, reservation):
        result = self.model.update(**reservation).where(self.model.id == reservation_id).execute()
        return result
