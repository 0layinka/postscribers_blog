from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class profileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default/default.png', upload_to='profile', validators=[FileExtensionValidator(['jpg', 'png'])])

    def __str__(self):
       return self.user.username