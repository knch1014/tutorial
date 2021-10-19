from django.urls import path
from .views import ActorListView, MovieListView

urlpatterns=[
    path("/actors", ActorListView.as_view()),
    path("/movies", MovieListView.as_view())
]


