from django.shortcuts import render
from .models import mycontacts


# Create your views here.


def todo_list(request):
    todos = mycontacts.objects.all
    return render(request, "mycontacts/todo_list.html", {"todos": todos})
