from django.urls import path
from post.views import time, portfolio

urlpatterns = [
    path('time/', time, name='time'),
    path('portfolio/', portfolio, name='portfolio'),
]
