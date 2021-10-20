import json

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Owner, Dog

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
       
        results = [{"name" : owner.name, "email" : owner.email, "age" : owner.age, "dogs" : [{"name" : dog.name, "age" : dog.age} for dog in owner.owners.all()]} for owner in Owner.objects.all()]

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
       
        results = [{'name' : dog.name, 'age' : dog.age, 'owner' :[{'name' : dog.owner.name}]} for dog in Dog.objects.all()]

        return JsonResponse({'result':results}, status=200)
            


	     
        
