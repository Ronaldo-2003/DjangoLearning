from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'Masala'),
        ('KL' , 'Kiwi'),
        ('PL' , 'Plain'),
        ('GR' , 'Ginger'),
        ('EL' , 'Elaichi'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2 , choices=CHAI_TYPE_CHOICE)

    class Meta:
        verbose_name = "Chai Variety"  # Singular form
        verbose_name_plural = "Chai Variety"  # Also singular(or it will automatically try to make it plural)

    def __str__(self):
        return self.name