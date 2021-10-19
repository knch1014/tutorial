from django.shortcuts import render
import json
from .models import Actor, Movie
from django.views import View
from django.http import JsonResponse, HttpResponse

# Create your views here.

class ActorListView(View):
    
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"],
        )
        return JsonResponse({'Message' : 'Created'}, status = 201)

    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            title = list(Movie.objects.filter(actors=actor).values('title'))   
            results.append(
                {
                    'first_name' : actor.first_name,
                    'last_name' : actor.last_name,
                    'titles' : title
                }
            )
        return JsonResponse({'result':results}, status=200)

class MovieListView(View):
    
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"],
        )
        return JsonResponse({'Message' : 'Created'}, status = 201)

    def get(self, request):
        movies = Movie.objects.all()
        results= []
        for movie in movies:
            name =list(Actor.objects.filter(movie_actor=movie).values('last_name','first_name'))
            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "name" : f'{name[0]["last_name"]}{name[0]["first_name"]}'
                }
            )
        return JsonResponse({'result':results}, status=200)

            
