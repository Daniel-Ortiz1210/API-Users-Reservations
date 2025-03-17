from peewee import CharField, IntegerField,DateTimeField, AutoField
from datetime import datetime

from src.database.connection import PostgresqlModel

class ReservationsModel(PostgresqlModel):
    destination = CharField(max_length=255, null=False)
    scheduled_at = DateTimeField(null=False, formats=["%Y-%m-%dT%H:%M"])
    created_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    updated_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])

    class Meta:
        table_name = 'reservations'
