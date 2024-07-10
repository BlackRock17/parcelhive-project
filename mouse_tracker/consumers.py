import json
import base64
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.files.base import ContentFile
from .models import MouseClick
from channels.db import database_sync_to_async

logger = logging.getLogger(__name__)


class MouseTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    @database_sync_to_async
    def save_mouse_click(self, x, y, photo):
        mouse_click = MouseClick(x=x, y=y, photo=photo)
        mouse_click.save()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'type' in text_data_json and text_data_json['type'] == 'photo':
            image_data = text_data_json['image']
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

            await self.save_mouse_click(self.last_x, self.last_y, data)

            await self.send(text_data=json.dumps({
                'message': 'Photo received and processed'
            }))

            logger.info(f"Photo taken on coordinates: x={self.last_x}, y={self.last_y}")
        else:
            x = text_data_json['x']
            y = text_data_json['y']

            self.last_x = x
            self.last_y = y

            await self.send(text_data=json.dumps({
                'message': 'Coordinates received'
            }))