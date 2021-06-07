from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializer import ToDoSerializer
from .models import ToDo
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


#any user views
class UserToDoView(ViewSet):
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, id):
        try:
            data = ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return Response({'message': 'The resource does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        data = ToDoSerializer(data)
        return Response(data.data, status=status.HTTP_200_OK)
    @action(method=['GET'],detail=True)
    def getall(self,request):
        data = ToDo.objects.all()
        data = ToDoSerializer(data, many=True)
        return Response(data.data, status=status.HTTP_200_OK)


#admin views
class ToDoView(ViewSet):
    permission_classes = [IsAuthenticated,IsAdminUser]
    def put(self, request, id):
        try:
            data = ToDo.objects.get(id=id)
        except Exception as e:
            return Response({'error': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
        data = ToDoSerializer(data, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
    def delete(self, request, id):
        try:
            data = ToDo.objects.get(id=id).delete()
        except Exception as e:
            return Response({'error': 'failed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Sucessfully Deleted'}, status=status.HTTP_200_OK)
    def create(self, request, id):
        try:
            data = ToDo.objects.create(**request.data)
        except Exception as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
        data = ToDoSerializer(data)
        return Response(data.data, status=status.HTTP_200_OK)