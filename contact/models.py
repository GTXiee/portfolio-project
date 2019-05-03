from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
