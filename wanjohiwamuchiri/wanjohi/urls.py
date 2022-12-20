from django.urls import path
from .views import portfolio

app_name = "wanjohi"

urlpatterns = [
    path('', portfolio, name='portfolio'),
]
