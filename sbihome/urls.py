from django.urls import path

from . import views

app_name = 'sbihome'

urlpatterns = [
    path('', views.index, name="index"),
]




# urlpatterns = [
#     path('', index, name='index'),
# ]