from django.db import models

# Create your models here.
class UserProfile(models.Model):
    
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chest_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hip_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    skin_tone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    captured_image = models.TextField(blank=True, null=True)  # Base64 or file path for the captured image

    def __str__(self):
        return f"{self.gender} - {self.skin_tone}"
