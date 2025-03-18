from peewee import CharField, ForeignKeyField, IntegerField
from datetime import datetime

from src.database.connection import PostgresqlModel
from src.database.models.fields import DateTimeField
from src.database.models.passengers import PassengersModel

class ReservationsModel(PostgresqlModel):
    destination = CharField(max_length=255, null=False)
    scheduled_at = DateTimeField(null=False, formats=["%Y-%m-%dT%H:%M"])
    created_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    updated_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    passenger_id = ForeignKeyField(PassengersModel, backref='reservations', on_update='CASCADE', on_delete='CASCADE')
    class Meta:
        table_name = 'reservations'
