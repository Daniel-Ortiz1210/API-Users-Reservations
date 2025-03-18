from src.database.models.passengers import PassengersModel
from src.database.connection import PostgresqlDatabase

from datetime import datetime

from peewee import DoesNotExist

class PassengersRepository:
    """
    Repository class for managing passenger data in the database.

    Attributes:
        db (PostgresqlDatabase): The database connection instance.
        model (PassengersModel): The model representing the passengers table.

    Methods:
        get_passengers(skip: int = 0, limit: int = 100):
            Retrieves a list of passengers from the database with pagination.
            Args:
                skip (int): The number of records to skip. Default is 0.
                limit (int): The maximum number of records to return. Default is 100.
            Returns:
                list: A list of passenger records.

        get_passenger(passenger_id: int):
            Retrieves a single passenger record by its ID.
            Args:
                passenger_id (int): The ID of the passenger to retrieve.
            Returns:
                dict: A dictionary representing the passenger record, or None if not found.
    """
    def __init__(self, db: PostgresqlDatabase):
        self.db = db
        self.model = PassengersModel

    def get_passengers(self):
        result = self.model.select(self.model.id, self.model.name).dicts()
        return list(result)

    def get_passenger(self, passenger_id: int):
        try:
            return self.model.select(
                self.model.id
            ).where(self.model.id == passenger_id).dicts().get()
        except DoesNotExist as e:
            return None
