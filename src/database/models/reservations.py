from peewee import CharField, IntegerField,DateTimeField, AutoField, Field
from datetime import datetime

from src.database.connection import PostgresqlModel

class DateTimeField(DateTimeField):

    def db_value(self, value):
        return super().db_value(value)
    
    def python_value(self, value):
        return value.strftime("%Y-%m-%dT%H:%M")

class ReservationsModel(PostgresqlModel):
    destination = CharField(max_length=255, null=False)
    scheduled_at = DateTimeField(null=False, formats=["%Y-%m-%dT%H:%M"])
    created_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    updated_at = DateTimeField(default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])

    class Meta:
        table_name = 'reservations'
