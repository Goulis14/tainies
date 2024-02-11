from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from .views import user_login

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home', views.home, name='home'),
    path('movie/<int:pk>', views.movie_detail, name='movie_detail'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
