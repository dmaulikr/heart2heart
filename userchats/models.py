from django.db import models
from heartuser.models import HeartUser
# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(HeartUser)

    def __str__(self):
        return str(self.chat_id)

class ChatLine(models.Model):
    chat_id = models.ForeignKey(Chat)
    user = models.ForeignKey(HeartUser)
    message = models.TextField()
    created_at = models.DateTimeField()

