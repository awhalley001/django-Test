from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, DocumentForm
from .handleuploadedfile import handle_uploaded_file
from .pulldb import DbClass

db = DbClass()

# Create your views here.
def index(response, id):
    ls = db.providetrackstable()
    return render(response, "maintest/yard.html", {"ls":ls})

def home(response):
    if response.method == 'POST':
        form = DocumentForm(response.POST, response.FILES)
        if form.is_valid():
            handle_uploaded_file(response.FILES['file'])
            return HttpResponseRedirect('yard')
    else:
        form = DocumentForm()
    return render(response, 'maintest/home.html', {'form': form})

def create(response):
    ls = db.providecarstable()
    return render(response, "maintest/create.html", {"ls": ls})

def yard(response):
    ls = db.providetrackstable()
    return render(response, "maintest/yard.html", {"ls": ls})

