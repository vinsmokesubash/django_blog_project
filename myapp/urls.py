from django.urls import path, include
from .views import  (
    index_view,
    details, 
    old_url_redirect,
    newurl, 
    PostView,
    contact,
    about
)


app_name = 'myapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('post/<str:slug>', details, name='details'),
    path('old_url/', old_url_redirect, name='old_url'),
    path("new_url/",newurl, name='new_url'),
    path('crud/', PostView.as_view(), name='post_list'),  # For list view
    path('crud/<int:post_id>/', PostView.as_view(), name='post_detail'),  # For detail view
    path('contact/',contact, name= 'contact'),
    path('about/', about, name='about')

]

