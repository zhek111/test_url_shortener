from django.db import models
import string
import random

MAX_LENGTH = 6


class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_token = models.CharField(max_length=MAX_LENGTH, unique=True)
    clicks = models.PositiveIntegerField(default=0)

    @classmethod
    def generate_token(cls):
        chars = string.ascii_letters + string.digits

        while True:
            token = ''.join(random.choice(chars) for _ in range(MAX_LENGTH))
            if not cls.objects.filter(short_token=token).exists():
                return token

    def increment_clicks(self):
        self.clicks = models.F('clicks') + 1
        self.save()

    @classmethod
    def custom_create(cls, url):
        short_token = cls.generate_token()
        return cls.objects.create(original_url=url, short_token=short_token)
