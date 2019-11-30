from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=20)
    url=models.URLField()
    publicationDate=models.DateTimeField()
    votes_total=models.IntegerField(default=1)
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    body=models.TextField()
    hunter= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_Date(self):
        return self.publicationDate.strftime('%b %d %Y')