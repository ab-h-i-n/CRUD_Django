from django.shortcuts import render
from .models import MovieInfo
from .forms import MovieForm
# Create your views here.


def home_Page(request):
    return render(request, 'home.html')


def create_Page(request):
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
            movies = MovieInfo.objects.all()
            return render(request, 'list.html', {'movie': movies})
    else:
        frm = MovieForm()
    return render(request, 'create.html', {'frm': frm})


def list_Page(request):
    movies = MovieInfo.objects.all()
    return render(request, 'list.html', {'movie': movies})


def delete(request, pk):
    movie = MovieInfo.objects.get(pk=pk)
    movie.delete()

    movies = MovieInfo.objects.all()
    return render(request, 'list.html', {'movie': movies})


def edit(request, pk):
    movie = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm = MovieForm(request.POST, instance=movie)
        if frm.is_valid():
            frm.save()
            movies = MovieInfo.objects.all()
            return render(request, 'list.html', {'movie': movies})
    else:
        frm = MovieForm(instance=movie)
    frm = MovieForm(instance=movie)
    return render(request, 'create.html', {'frm': frm})
