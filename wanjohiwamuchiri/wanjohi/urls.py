from django.urls import path
from .views import index

app_name = "wanjohi"

urlpatterns = [
    path('index/', index, name='index'),
]
