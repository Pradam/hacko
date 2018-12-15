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


class HistoryData(BaseContent):
    age = models.PositiveIntegerField()
    gender = models.TextField(editable=False)
    name = models.CharField(max_length=255, unique=True)


class HistoryData(BaseContent):

    ALCOHOL_CHOICES = (
        (1, 'NO'),
        (2, 'OCCATIONALLY'),
        (3, 'HEAVY')
    )

    SMOKING_CHOICES = (
        (1, 'NO'),
        (2, 'MODERATE'),
        (3, 'CHAIN')
    )


    CLAIM_CHOICES = (
        (1, 'NO CLAIM'),
        (2, 'REJECTED'),
        (3, 'ACCEPTED')
    )

    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'TRANSGENDER')
    )

    aadhar_id = models.IntegerField()
    name = models.TextField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    premium = models.PositiveIntegerField()
    coverage = models.PositiveIntegerField()
    is_alcoholic = models.IntegerField(choices=ALCOHOL_CHOICES, default=1)
    is_smoker = models.IntegerField(choices=SMOKING_CHOICES, default=1)
    claimed = models.IntegerField(choices=CLAIM_CHOICES, default=1)

    class Meta:
        unique_together = ('aadhar_id',)

    def __str__(self):
        return self.aadhar_id