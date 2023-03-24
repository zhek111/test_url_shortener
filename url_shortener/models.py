from django.db import models
import string
import random


class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_token = models.CharField(max_length=6, unique=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_token:
            self.short_token = self.generate_token()
        super().save(*args, **kwargs)

    def generate_token(self):
        chars = string.ascii_letters + string.digits

        while True:
            token = ''.join(random.choice(chars) for _ in range(6))
            if not ShortenedURL.objects.filter(short_token=token).exists():
                return token

    def increment_clicks(self):
        self.clicks += 1
        self.save()
