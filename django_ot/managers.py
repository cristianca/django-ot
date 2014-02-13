from django.db import models


class OtConfigManager(models.Manager):

    def activated(self):
        return self.all().filter(is_active=True)