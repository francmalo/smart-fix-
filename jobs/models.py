import uuid
from django.db import models
from accounts.models import Account


class Job(models.Model):
    ROLES = [
        ('assigned', 'assigned'),
        ('pending', 'pending'),
        ('completed ', 'completed'),

    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.IntegerField()
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=200)
    status = models.CharField(
        max_length=200, blank=True, choices=ROLES, default='pending')
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    technician = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.job}'
