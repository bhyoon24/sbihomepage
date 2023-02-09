from django.urls import path

from . import views
app_name = 'sbihome'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('sms', views.sms, name="sms"),
]




# urlpatterns = [
#     path('', index, name='index'),
# ]