from .models import Owner, Dog

from django.views import View
from django.http import HttpResponse

import json

# Create your views here.

class OwnerListView(View):

    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data["name"],
            email = data["email"],
            age = data["age"],
        )
        
        return HttpResponse(201)
   
    def get(self, request):
       owners = Owner.objects.all()
       results = []

       for owner in owners:
           results.append(
               {
                   "name" : owner.name,
                   "email" : owner.email,
                   "age" : owner.age,
               }
           )

class DogListView(View):

    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data["name"],
            owner_id = Owner.objects.get(id= data["owner_id"]),
            age = data["age"],
        )

        return HttpResponse(201)


    def get(self, request):
       dogs = Dog.objects.all()
       results = []

       for owner in owners:
           results.append(
               {
                   "name" : dog.name,
                   "owner" : dog.owner.name,
                   "age" : dog.age,
               }
           )


	     
        
