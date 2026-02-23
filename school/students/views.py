from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def student_list(request):

  if request.method=='GET':
    ordering = request.query_params.get('ordering')
    search=request.query_params.get('search')
    students=Student.objects.all()
    age=request.query_params.get('age')
    name=request.query_params.get('name')
    if age: 
      students=students.filter(age=age)
    if name:
      students=students.filter(name__icontains=name)
    if ordering:
      students=students.order_by(ordering)
    paginator=PageNumberPagination()
    paginator.page_size=2
    paginated_students=paginator.paginate_queryset(students, request)
    serializer=StudentSerializer(paginated_students,many=True)
    return paginator.get_paginated_response(serializer.data)
  if request.method=='POST':
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=201)
  return Response(serializer.error, status=400)
@api_view(['GET','PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def student_detail(request,id):
  try:
    student=Student.objects.get(id=id)
  except Student.DoesNotExist:
    return Response({'error':'Not Found'},status=404)

  if request.method=='GET':
    serializer=StudentSerializer(student)
    return Response(serializer.data)
  if request.method=='PUT':
    serializer=StudentSerializer(student,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=400)
  if request.method=='DELETE':
    student.delete()
    return Response({'message':'delete'})
  if request.method=='PATCH':
    serializer=StudentSerializer(student,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=400)

