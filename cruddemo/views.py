from django.http import JsonResponse
from .models import student
from .serializers import studentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def student_list(request,format=None):
    if request.method=='GET':
        students=student.objects.all()
        serializer=studentSerializer(students,many=True)
        return JsonResponse({'students list':serializer.data},safe=False)
    if request.method=='POST':
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def student_details(request,id,format=None):
    try:
        students=student.objects.get(pk=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=studentSerializer(students)
        return Response(serializer.data)  
    elif request.method=='PUT':
        serializer=studentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        pass
