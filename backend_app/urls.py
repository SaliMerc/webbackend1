from django.urls import path
from .import views

urlpatterns=[
    path('',views.blog,name='_my_blog'),
    path('<int:id>', views.blog_details, name='my_blog_details'),
]