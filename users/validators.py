from django.core.exceptions import ValidationError


class CustomPasswordValidation:

    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError('There must be a digit in your password')

    def get_help_text(self):
        return 'Your password must contain at least 1 digit'
