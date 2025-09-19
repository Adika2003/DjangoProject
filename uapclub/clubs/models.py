from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='clubs/logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

