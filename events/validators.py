from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date


def validate_future_date(value):
    if isinstance(value, date):
        if value < timezone.now().date():
            raise ValidationError(
                'Date cannot be in the past. Please select a future date.'
            )