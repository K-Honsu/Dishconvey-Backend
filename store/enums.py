from django.db.models import TextChoices

class PaymentStatus(TextChoices):
    PENDING = 'PENDING'
    SUCCESSFUL = 'SUCCESS'
    FAILED = 'FAILED'