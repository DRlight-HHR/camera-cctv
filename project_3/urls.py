from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .main_app import sing_up, log_in, log_out, home_, check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sing_up),
    path('login/', log_in),
    path('long_out/', log_out),
    path('home/', home_),
    path('check/', check),
    path('book/', include('test_app.urls')),
    path('rest/', include('rest.urls'))
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
