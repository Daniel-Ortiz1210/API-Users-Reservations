from boto3 import client
from src.utils.config import Config

settings = Config()

class SQSService:
    def __init__(self):
        self.client = client('sqs')

    def send_message_to_queue(self, message: dict):
        response = self.client.send_message(
            QueueUrl=settings.queue_url,
            MessageBody='Helo world'
        )
        print(response)

        return response
    