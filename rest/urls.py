from django.urls import path
from .views import check_off_on, get, maker, search, post_photo, delete_data, deletedata, movie, movie_get, delete_movie

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get/', get.as_view()),
    path('check/', check_off_on.as_view()),
    path('get-movie/', movie_get.as_view()),
    path('make/', maker.as_view()),
    path('post/', post_photo.as_view()),
    path('movie/<pk>/', movie.as_view()),
    path('search/', search.as_view()),
    path('delete2/', deletedata),
    path('delete_movie/<pk>/', delete_movie.as_view()),
    path('login/', obtain_auth_token, name='api-tokn-auth'),
    path('delete/<id>', delete_data.as_view())
]
