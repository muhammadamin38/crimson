from django.db import models

# Create your models here.
class Rang(models.Model):
    nomi = models.CharField(max_length=30)
    
    
    def __str__ (self) -> str:
        return self.nomi

class Moshin(models.Model):
    nomi = models.CharField(max_length=20)
    rang = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)

    def __str__ (self) -> str:
        return self.nomi