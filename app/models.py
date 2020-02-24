from django.db import models

# Create your models here.
class SearchModel(models.Model):
    company_name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=50)
    headquater = models.CharField(max_length=100)
    founder = models.CharField(max_length=40)

