from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request):
    author = Author.objects.all()
    return render(request, 'author/home.html', {'author' : author})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'author/register.html', {'form' : RegistrationForm()})

def update(request, id):
    author = Author.objects.get(id = id)
    form = RegistrationForm(instance=author)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'author/update.html', {'form' : form })

def delete(request, id):
    author = Author.objects.get(id = id)
    author.delete()
    return redirect('home')

def profile(request, id):
    author = Author.objects.get(id = id)
    return render(request, 'author/profile.html', {'author' : author })