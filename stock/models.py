from django.db import models
from django.contrib.auth.models import User

# Create your models here.

cat = [
    ('1', 'Agric_prod'),
    ('2', 'Manufactured'),
]

class CustomerStock(models.Model):
    owner = models.ForeignKey(User, related_name='CustomerStock', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    category = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f'{self.owner} CustomerStock'

