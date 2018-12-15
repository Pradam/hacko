from django.contrib.postgres.fields import JSONField
from django.db import models

OPTIONAL = {'blank': True, 'null': True}

ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)

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

MEMBER_CHOICES = (
    (1, 'YES'),
    (2, 'NO'),
    (3, 'PENDING')
)

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


    aadhar_id = models.BigIntegerField()
    name = models.TextField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    coverage = models.BigIntegerField(default=0)
    is_alcoholic = models.IntegerField(choices=ALCOHOL_CHOICES, default=1)
    is_smoker = models.IntegerField(choices=SMOKING_CHOICES, default=1)
    claimed = models.IntegerField(choices=CLAIM_CHOICES, default=1)
    is_member = models.IntegerField(choices=MEMBER_CHOICES, default=1)
    class Meta:
        unique_together = ('aadhar_id',)

    def __str__(self):
        return self.aadhar_id