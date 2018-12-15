from django.contrib.postgres.fields import JSONField
from django.db import models

OPTIONAL = {'blank': True, 'null': True}

ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)


class BaseContent(models.Model):
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def switch(self):
        self.active = {2: 0, 0: 2}[self.active]
        self.save()

    def __str__(self):
        return self.name
