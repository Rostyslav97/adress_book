from django.db import models
from django.urls import reverse

class Person(models.Model):
    name_surname = models.CharField(max_length=200)
    # author = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.CASCADE,
    #     )
    adress = models.TextField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name_surname
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    