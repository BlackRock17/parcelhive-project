from django.db import models


class MouseClick(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    photo = models.ImageField(upload_to='mouse_clicks/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Click at ({self.x}, {self.y}) on {self.timestamp}"
