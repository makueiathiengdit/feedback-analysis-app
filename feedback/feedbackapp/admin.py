from django.contrib import admin
from .models import Feedback, AIModel, TextGen
# Register your models here.



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('time_created', 'message', 'label', 'score')
   
@admin.register(TextGen)
class TextGenAdmin(admin.ModelAdmin):
    list_display = ('time_created', 'prompt', 'generated_text')
   
@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'model_name', 'status', 'created_at', 'use_count', 'last_used_date')
   

