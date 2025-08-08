from django.db import models
from django.utils import timezone

class Task(models.Model):
    ASSIGNEE_CHOICES = [
        ('A', 'Peter'),
        ('B', 'Isabelle'),
        ('BOTH', 'Beide'),
    ]

    title = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    assignee = models.CharField(max_length=4, choices=ASSIGNEE_CHOICES)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title