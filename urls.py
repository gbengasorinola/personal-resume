from django.urls import path

from .views import index_view

urlpatterns = [
    path('', home_view),
]

from django.shortcuts import render

def home_view(request):
    print(request.POST)
    return render(request, "index.html")