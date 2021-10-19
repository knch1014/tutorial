from .models import Owner, Dog

from django.views import View
from django.http import JsonResponse, HttpResponse

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
        return JsonResponse({'Message':'Created'}, status=201)
   
    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
         
            dogs=list(Dog.objects.filter(owner=owner).values("name","age"))
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age,
                    "dogs" : dogs
                }
            )
        return JsonResponse({'result':results}, status=200)

class DogListView(View):

    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name = data["name"],
            owner_id = Owner.objects.get(id= data["owner_id"]),
            age = data["age"],
        )
        return JsonResponse({'Message':'Created'}, status=201)


    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "owner" : dog.owner.name,
                    "age" : dog.age,
                }
            )
        return JsonResponse({'result':results}, status=200)
            


	     
        
