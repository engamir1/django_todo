from django.shortcuts import redirect, render

# Create your views here
from .models import Task


def home(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "task/home.html", context)


def add_task(request):
    task = request.POST["task"]
    Task.objects.create(task=task)
    return redirect("home")
