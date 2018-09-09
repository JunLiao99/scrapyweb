from django.urls import path
from . import views
import django.urls

app_name="news"


urlpatterns = [
    path('',views.index),
    path('scrapy/',views.scrapy),
    path('go_dic/', views.news , name='go_dic'),
    #localhost/res/res => booking.html
    # path('booking/',views.booking),
    # path('lightbox/',views.box)
]