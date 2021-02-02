from django.contrib import admin
from django.urls import path, include
from home import views


#admin log-in customization

admin.site.site_header = "pushkR BOOKS_STORE"
admin.site.site_title = "Welcome to pushk Dashboard"
admin.site.index_title = "Welcome to my BOOKS_STORE"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sign', views.sign, name='sign'),
    path('popular', views.popular, name='popular'),
]