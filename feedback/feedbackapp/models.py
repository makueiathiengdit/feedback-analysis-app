from django.db import models

import random


def generate_id(length=10):
    id = '11'
    
    for _ in range(length):
        id += str(random.randint(0, 9))
        
    return id   
    
    
       
class Feedback(models.Model):
    message = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=50, null=True)
    score = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.time_created} \t\t {self.message}"
    
    list_display = ['time_created', 'message', 'label', 'score' ]  
    
    class Meta:
        ordering = ('-time_created', 'time_created')

    
  
  

class TextGen(models.Model):
    prompt = models.TextField()
    time_created = models.DateField(auto_now_add=True)
    generated_text = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.time_created} {self.prompt} {self.generated_text}"   
    
    class Meta:
        ordering = ['-time_created', 'time_created']

    
# 
class AIModel(models.Model):
    STATUS_CHOICES = [('1', 'AVAILABLE'),('0', 'UNAVAILABLE')]
    
    model_id = models.CharField(max_length=12, default=generate_id)
    model_name = models.CharField(max_length=50)
    status = models.CharField(max_length=1,  choices=STATUS_CHOICES)   
    created_at = models.DateField(auto_now_add=True)
    last_used_date = models.DateTimeField(auto_now_add=True)
    use_count = models.IntegerField(default=0)
      
      
    def __str__(self) -> str:
        return f"{self.model_name} \t {self.status} \t {self.created_at} \t {self.use_count} \t {self.last_used_date}"  
    
      
class TextClassifier(models.Model):
    text = models.TextField()
    category = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.time_created} \t {self.text}"    