from django.core.exceptions import ValidationError
from django.urls import path


def validator_only_letters_numbers_and_underscore(value):
    for letter in value:
        if not letter.isalpha and letter.isdigit() and letter != '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
