from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.about, name="contact" ),
    path('count/', views.count, name="count"),
    path('', views.home, name="home"),
]
