from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

class City(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    STATUS = [
        ('NEW','New'),
        ('GOOD','Good'),
        ('NOT_BAD','Not Bad'),
        ('BAD','Bad')
    ]
    

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    desc = models.TextField()
    author = models.CharField(max_length=200)
    status = models.CharField(choices=STATUS,default="NOT_BAD")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    location = models.CharField(max_length=300,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_free = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Trade(models.Model):

    STATUS = [
        ('PENDING','Pending'),
        ('REJECTED','Rejected'),
        ('ACCEPTED','Accepted'),
        ('RETURNED','Returned'),
        ]
    
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    getter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    trade_at = models.DateTimeField(auto_now=True)
    start_data =models.DateTimeField(auto_now=True)
    finish_data =models.DateTimeField()
    status = models.CharField(choices=STATUS,default="PENDING")


class Review(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='written_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)






