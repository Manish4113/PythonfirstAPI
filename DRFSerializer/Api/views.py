from django.shortcuts import render
from .models import Student
# Create your views here.
from .serilizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from  django.http import HttpResponse,JsonResponse
#model object single student

def student_details(request,pk):
    stu=Student.objects.get(id=pk)
    #print(stu)
    serializer=StudentSerializer(stu)
   # print(serializer)
   # print(serializer.data)
   # json_data=JSONRenderer().render(serializer.data)
   # print(json_data)
    #return  HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

#query set all data
def student_list(request):
    stu=Student.objects.all()
    #print(stu)
    serializer=StudentSerializer(stu,many=True)
   # print(serializer)
   # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
   # print(json_data)
    return  HttpResponse(json_data,content_type='application/json')
