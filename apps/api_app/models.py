from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=255)  # Field to store the message

    def __str__(self):
        return self.text
