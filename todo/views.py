from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(["GET"])
def all(request):
    todos = Task.objects.all()
    serializer = TaskSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def incom(request):
    todos = Task.objects.filter(complete=False)
    serializer = TaskSerializer(todos, many=True)
    return Response(serializer.data)
@api_view(["GET"])

def com(request):
    todos = Task.objects.filter(complete=True)
    serializer = TaskSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["DELETE"])
def delete(request, pk):
    todo = Task.objects.get(id=pk)
    todo.delete()
    return Response("Delete Success")


@api_view(["PUT"])
def update(request, pk):
    todo = Task.objects.get(id=pk)
    serializer = TaskSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)