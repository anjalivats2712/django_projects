from django.contrib import admin
from django.urls import path
from .views import Homepage,Aboutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage.as_view(),name="Home"),
    path('about',Aboutpage.as_view(),name="About"),
]
