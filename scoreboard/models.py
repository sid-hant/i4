from django.db import models

# Create your models here.
class scoreBoard(models.Model):
    team_name = models.TextField()
    team_score = models.TextField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-team_score']