import base64

from cryptography.fernet import Fernet
from django import forms
from django.conf import settings
from django.db import models


def _get_fernet():
    key = getattr(settings, "FIELD_ENCRYPTION_KEY", None)
    if not key:
        key_b64 = base64.urlsafe_b64encode(b"infracore-demo-credentials-32byt")
        key = key_b64.decode()
    return Fernet(key)


class EncryptedTextField(models.TextField):
    description = "A TextField that encrypts values at rest using Fernet"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        f = _get_fernet()
        return f.decrypt(value.encode()).decode()

    def to_python(self, value):
        if value is None or isinstance(value, str):
            return value
        return str(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        f = _get_fernet()
        return f.encrypt(value.encode()).decode()

    def formfield(self, **kwargs):
        kwargs.setdefault("widget", forms.PasswordInput(render_value=True))
        return super().formfield(**kwargs)
