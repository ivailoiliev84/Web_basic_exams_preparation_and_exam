from django.db import models


# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20
    )

    last_name = models.CharField(
        max_length=20
    )

    age = models.IntegerField()

    image_url = models.URLField(
        blank=True,
    )


class Note(models.Model):
    title = models.CharField(
        max_length=30
    )
    image_url = models.URLField(
        blank=True,
    )

    content = models.TextField()

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )