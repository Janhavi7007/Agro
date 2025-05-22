# agroapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150,default='Unknown')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    USERNAME_FIELD = 'username'  # You can change to 'email' if you prefer email login
    REQUIRED_FIELDS = ['email', 'full_name']  # These are required when using createsuperuser

    def __str__(self):
        return self.username
    

from django.db import models

class GovernmentScheme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    apply_link = models.URLField()
    state = models.CharField(max_length=100)  # e.g., 'Maharashtra'

    def __str__(self):
        return f"{self.title} ({self.state})"


from django.db import models

class AgroBusiness(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='agro_business_images/')
    description = models.TextField()
    cost_to_implement = models.CharField(max_length=200)
    benefits = models.TextField()
    profit = models.CharField(max_length=200)
    loss = models.TextField(blank=True, null=True)
    side_business = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


from django.db import models

class OrganicFarmingCategory(models.Model):
    title = models.CharField(max_length=100)  # Category ka naam
    description = models.TextField()  # Category ka description
    benefits = models.TextField()  # Benefits related to the category
    image = models.ImageField(upload_to='media/agro_business_images/', blank=True, null=True)  # Image for the category (optional)
    slug = models.SlugField(unique=True)  # Slug for SEO-friendly URL

    def __str__(self):
        return self.title


from django.db import models
from django.conf import settings

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_first_time = models.BooleanField()
    reason = models.TextField()
    found_what_needed = models.BooleanField()
    user_friendliness = models.IntegerField()  # 1 to 5 stars
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_reply = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.user.username} - Feedback on {self.submitted_at.strftime('%Y-%m-%d')}"
    


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
