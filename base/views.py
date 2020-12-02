from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Person

# Create your views here.


def index(request):

    posts = Post.objects.all()
    people = Person.objects.all()

    context = {
        "posts": posts,
        "people": people,
    }

    return render(request, 'index.html', context)
