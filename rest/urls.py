from django.urls import path
from .views import get, maker, search, delete_data, deletedata, movie, movie_get

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get/', get.as_view()),
    path('get-movie/<pk>/', movie_get.as_view()),
    path('make/', maker.as_view()),
    path('movie/<pk>/', movie.as_view()),
    path('search/', search.as_view()),
    path('delete2/', deletedata),
    path('login/', obtain_auth_token, name='api-tokn-auth'),
    path('delete/<id>', delete_data.as_view())
]
