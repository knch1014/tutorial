import json

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Actor, Movie

# Create your views here.

class ActorListView(View):
    

    def get(self, request):
        results = [
            {
                'name'   : f'{actor.last_name}{actor.first_name}', 
                'titles' : [{'title' : movie.title} for movie in actor.movie_actor.all()]
            } for actor in Actor.objects.all()
        ]
        
        return JsonResponse({'result' : results}, status=200)

class MovieListView(View):
    


    def get(self, request):
        results = [
            {
                "title"        : movie.title, 
                "running_time" : movie.running_time, 
                "name" : [{'first_name' : actor.first_name} for actor in movie.actors.all()]
            } for movie in Movie.objects.all()
        ]
       
        return JsonResponse({'result' : results}, status=200)
