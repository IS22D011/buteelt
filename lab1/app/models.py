from django.db import models

class Angilal(models.Model):
    aname=models.CharField(max_length=250,)

    def __str__(self):
        return self.aname
    

class Baraa(models.Model):
    name= models.CharField(max_length=250,)
    category=models.ForeignKey(Angilal, on_delete=models.CASCADE, related_name='product', null=True, blank=True)

    def __str__(self):
        return self.name
    