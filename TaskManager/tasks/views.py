from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from drf_yasg.utils import swagger_auto_schema
# ------------------------ Category ------------------------ #

class CategoryListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Отримати список усіх категорій",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Створити нову категорію",
        request_body=CategorySerializer,
        responses={201: CategorySerializer}
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Отримати категорію за ID",
        responses={200: CategorySerializer}
    )
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Оновити категорію за ID",
        request_body=CategorySerializer,
        responses={200: CategorySerializer}
    )
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Видалити категорію за ID",
        responses={204: 'Категорія успішно видалена'}
    )
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------ Task ------------------------ #

class TaskListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Отримати список усіх завдань",
        responses={200: TaskSerializer(many=True)}
    )
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Створити нове завдання",
        request_body=TaskSerializer,
        responses={201: TaskSerializer}
    )
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Отримати завдання за ID",
        responses={200: TaskSerializer}
    )
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Оновити завдання за ID",
        request_body=TaskSerializer,
        responses={200: TaskSerializer}
    )
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Видалити завдання за ID",
        responses={204: 'Завдання успішно видалене'}
    )
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)