from transformers import pipeline
# ChatBot = None
SentimentAnalyzer = None
TextGenerator = None
TextClassifier = None





try:
    # ChatBot = pipeline('sentiment-analysis')
    SentimentAnalyzer = pipeline('sentiment-analysis')
    TextGenerator = pipeline('text-generation')
    # TextClassifier = pipeline("text-classification", model="alimazhar-110/website_classification")
    
    print("Chatbot is ready")   
except Exception as e:
    print("error initialing chatbot")
    print(e)
    
from django.http import JsonResponse 
from django.shortcuts import render
from .models import Feedback, AIModel
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def index(request):
    data = {}
    if request.method == 'POST':
        data = request.POST
        try:
            message = data['message']
            model_id = data['model_id']
            
            if model_id == '116239551485':
                results = sentiment_analyzer(message)
                return JsonResponse(results)
            elif model_id == '117051717706':
                results = text_generator(message)
                return JsonResponse({"generated_text": results, 'model':'txt_gen'})
            else:
                results = sentiment_analyzer(message)
                
                return JsonResponse(results)    
                
        except Exception as e:
            print("error")
            print(e)
        
        # chat = Feedback.objects.create(message = message, label=data['label'], score=data['score'])
        # return JsonResponse({'message':chat.message, 'label':chat.label, 'score': chat.score})
        
    feedbacks = Feedback.objects.all()
    d = [{'message': feedback.message, 'label':feedback.label, 'score':feedback.score } for feedback in feedbacks][:5]
        
  
    return render(request, 'feedbackapp/index.html', {"feedbacks":d, 'models':get_models_from_db()})


def feedbacks(request, source='ajax'):
    feedbacks = Feedback.objects.all()
    d = [{'message': feedback.message, 'label':feedback.label, 'score':feedback.score } for feedback in feedbacks]
                
    return render(request, 'feedbackapp/feedbacks.html', {'feedbacks':d})


def text_generator(prompt):
    generated_text = TextGenerator(prompt)[0]['generated_text']
    # print(generated_text)
    return generated_text


def sentiment_analyzer(message):
      responses = SentimentAnalyzer(message)
      feedback = Feedback.objects.create(message = message, label=responses[0]['label'], score=responses[0]['score'])
      return {'message': message, 'label': feedback.label, 'score':feedback.score, 'model': 'sen-anl'}
      
def message_classifier(messgae):
    pass




def get_models_from_db(n=3):
    models = AIModel.objects.filter(status = '1')
    models = [{'name': model.model_name, 'id': model.model_id} for model in models]
    
    return models[:n]


def get_model_by_id(id):
    return AIModel.objects.get(model_id=id)
    
    