from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import JsonResponse
from .models import Card



class Index(generic.TemplateView):
    template_name = "index.html"



class ApiCartListView(generic.View):

    def get(self, request, *args, **kwargs):
        card_list = Card.objects.all()
        result = []

        for card in card_list:
            obj = {}
            obj["title"] = card.title
            obj["subtitle"] = card.subtitle
            obj["img"] = card.img.url
            obj["description"] = card.description
            result.append(obj)
        return JsonResponse(result, safe=False)