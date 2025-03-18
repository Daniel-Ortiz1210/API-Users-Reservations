from src.database.connection import PostgresqlDatabase
from src.database.models.reservations import ReservationsModel

from datetime import datetime

from peewee import DoesNotExist

class ReservationsRepository:
    """
    ReservationsRepository is a repository class for handling CRUD operations on reservations in the database.
    Attributes:
        db (PostgresqlDatabase): The database connection instance.
        model (ReservationsModel): The model class representing the reservations table.
    Methods:
        get_reservations():
            Retrieves all reservations from the database.
            Returns:
                list: A list of dictionaries representing the reservations.
        create_reservation(reservation: dict):
            Creates a new reservation in the database.
            Args:
                reservation (dict): A dictionary containing reservation details.
            Returns:
                ReservationsModel: The created reservation instance.
        get_reservation(reservation_id: int):
            Retrieves a specific reservation by its ID.
            Args:
                reservation_id (int): The ID of the reservation to retrieve.
            Returns:
                dict: A dictionary representing the reservation, or None if not found.
        update_reservation(reservation_id: int, reservation: dict):
            Updates an existing reservation in the database.
            Args:
                reservation_id (int): The ID of the reservation to update.
                reservation (dict): A dictionary containing updated reservation details.
            Returns:
                int: The number of rows updated.
        delete_reservation(reservation_id: int):
            Deletes a reservation from the database.
            Args:
                reservation_id (int): The ID of the reservation to delete.
            Returns:
                int: The number of rows deleted.
    """
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
    