from django.db import models

class Gaming(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)
    user = models.CharField(max_length= 20)
       
    def __str__(self):
        return self.name
    
    
class Crypto(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)
    user = models.CharField(max_length= 20)
     
    def __str__(self):
        return self.name
    

class Coding(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)
    user = models.CharField(max_length= 20)
       
    def __str__(self):
        return self.name
    

class Anime(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)  
    user = models.CharField(max_length= 20)  
    
    def __str__(self):
        return self.name
