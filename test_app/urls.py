from django.urls import path
from .views import home, home_d, vid, deletee

urlpatterns = [
    path('main/home/', home),
    path('delete/', deletee),
    path('main/home/vid/', vid),
    path('main/home/book/<pk>/<name>/', home_d)
]
