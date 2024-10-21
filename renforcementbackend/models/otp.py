from django.contrib.auth.models import User
from django.db import models
import random

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.save()
    
    def is_valid(self):
        return True
