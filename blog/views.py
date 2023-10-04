from django.shortcuts import render
from django.http import HttpResponse

posts =[{
    'author': 'Israa',
    'title' : 'First Post',
    'date_posted'  : 'Oct 3, 2023',
    'content': 'First Try with dummy data'
    },
    {
    'author': 'Rohin',
    'title' : 'Second Post',
    'date_posted'  : 'Oct 3, 2023',
    'content': 'Its good to do Django'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

