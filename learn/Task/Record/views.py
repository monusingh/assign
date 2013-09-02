from django.shortcuts import render_to_response
from Record.models import Movie
from django.template import RequestContext
from django.contrib import auth

def getMovies(request, selected_page=1):
   
    movies = Movie.objects.all().order_by('-date')

    return render_to_response('movies.html',dict(movies=movies, user=request.user))


def home(request):
    return render_to_response('home.html')

def login_view(request):
    username = request.MOVIE.get('username', '')
    password = request.MOVIE.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")


