from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_utem_email(value):
    """
    Validates that email belongs to UTeM domain.
    Accepts: @student.utem.edu.my, @utem.edu.my
    """
    # UTeM email patterns
    allowed_domains = [
        r'@student\.utem\.edu\.my$',
        r'@utem\.edu\.my$',
    ]

    is_valid = any(re.search(pattern, value.lower()) for pattern in allowed_domains)

    if not is_valid:
        raise ValidationError(
            _('%(value)s is not a valid UTeM email address. Please use your @student.utem.edu.my or @utem.edu.my email.'),
            params={'value': value},
        )
    return value