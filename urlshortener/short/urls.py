from django.urls import path
from short import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('shorten', views.short_url, name="ShortUrl"),
    path('<str:hash_id>', views.redirector, name="Redirector"),
]


