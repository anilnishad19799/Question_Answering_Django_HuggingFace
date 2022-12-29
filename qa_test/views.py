from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .qa_class import Question_Answer
import json
# Create your views here.

class_obj = Question_Answer()

@csrf_exempt
def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def predict(request):
    if request.method =='POST':
        json_data = json.loads(request.body)
        output = class_obj.process(json_data['context'],json_data['question'])
        final_output = {"context":json_data['context'] ,"question":json_data['question'], "answer":output['answer']}
        return HttpResponse(f"{final_output}")
