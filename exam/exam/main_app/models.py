from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from exam.main_app.validators import validator_only_letters_numbers_and_underscore


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validator_only_letters_numbers_and_underscore,
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )

    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30

    GENRE_MAX_LENGTH = 30

    PRICE_MIN_VALUE = 0

    POP_MUSIC = "Pop Music"
    DJAZZ_MUsIC = "Jazz Music"
    R_AND_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    TYPE_CHOICE = [(x, x) for x in (POP_MUSIC, DJAZZ_MUsIC, R_AND_B_MUSIC, ROCK_MUSIC,
                                    COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER_MUSIC)]

    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=TYPE_CHOICE,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )
