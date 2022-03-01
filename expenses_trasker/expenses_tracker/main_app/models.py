from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.
from expenses_tracker.main_app.validators import validator_only_letters, ValidatorMaxSizeInMB


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    IMAGE_MAX_SIZE = 5.0
    BUDGET_MIN_VALUE = 0


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_only_letters,
        )

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validator_only_letters,
        ),
    )
    budget = models.FloatField(
        default=0,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_image',
        validators=(
            ValidatorMaxSizeInMB(IMAGE_MAX_SIZE),
        )
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=30,
    )
    expense_image = models.URLField()

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField()
