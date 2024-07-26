from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def cat_index(request):
    cats = Cat.objects.all()
    # Render the cats/index.html template with the cats data
    return render(request, "cats/index.html", {"cats": cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {"cat": cat})

