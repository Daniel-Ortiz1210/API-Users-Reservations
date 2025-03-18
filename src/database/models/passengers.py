from peewee import CharField, IntegerField
from datetime import datetime

from src.database.connection import PostgresqlModel
from src.database.models.fields import DateTimeField

class PassengersModel(PostgresqlModel):
    name = CharField(max_length=255, null=False)
    age = IntegerField(null=False)
    email = CharField(max_length=255, null=False)
    created_at = DateTimeField(
        default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    updated_at = DateTimeField(
        default=datetime.now().isoformat(timespec="minutes"),formats=["%Y-%m-%dT%H:%M"])
    
    class Meta:
        table_name = 'passengers'

