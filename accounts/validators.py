from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^((\+7)|8)\d{10}$',
    message=(
        "Phone number must be entered in the format: "
        "'+79999999999' or '89999999999'."
    ))
