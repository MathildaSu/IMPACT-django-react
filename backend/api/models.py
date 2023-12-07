from django.db import models

# Create your models here.


class Note(models.Model):
    uuid = models.UUIDField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:100]

    class Meta:
        ordering = ["-created"]
