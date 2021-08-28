from django.db import models

# Create your models here.
class URL (models.Model):
    full_url = models.TextField()
    hashed = models.TextField(unique=True)
    
    class meta:
        db_table = 'url_shortner'
