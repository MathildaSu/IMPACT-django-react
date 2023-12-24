from django.db import models

class Nota(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    # status = models.CharField(
    #     max_length=12,
    #     blank=True,
    #     choices=[
    #         ("Completado", "Completado"),
    #         ("Detenido", "Detenido"),
    #         ("Pendiente", "Pendiente"),
    #     ]
    # )

    def __str__(self):
        return self.title