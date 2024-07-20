# from django.db import models
# from django.urls import reverse
# from django.contrib.auth.models import User


# class Books(models.Model):
#     title = models.CharField(max_length=125)
#     content = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     author = models.TextField(max_length=50)
    
#     def __str__(self):
#                 return self.title

#     def get_absolute_url(self):
#            return reverse('home')
    
#     class Comment(models.Model):    
#             book = models.ManyToManyField(Books)
#             user = models.ManyToManyField(User)
#             content = models.TextField()