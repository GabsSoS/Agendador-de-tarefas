from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ('iniciado', 'Em andamento'),
    ('em pausa', 'Pausado'),
    ('finalizado', 'Finalizado')
    
)

class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateField(default='')
    end_date = models.DateField()
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.title