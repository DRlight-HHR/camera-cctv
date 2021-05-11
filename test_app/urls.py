from django.urls import path
from .views import home, home_d, vid

urlpatterns = [
    path('main/home/', home),
    path('main/home/vid/', vid),
    path('main/home/book/<pk>/<name>/', home_d)
]
