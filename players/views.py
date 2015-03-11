from django.shortcuts import render
from django.views.generic import *
from .models import Players
# Create your views here.
class HomeView(TemplateView):
    template_name = 'main.html'

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {}
        context['pl'] = Players.objects.all().order_by('-lesions', '-wins', )
        return context


class ChampionshipView(TemplateView):
    template_name = 'championship.html'


    def dispatch(self, request, *args, **kwargs):
        return super(ChampionshipView, self).dispatch(request, *args, **kwargs)