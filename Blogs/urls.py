from . import views
from django.urls import path
urlpatterns = [
    path('home/',views.home, name='home'),
    path('detail/<int:blog_id>',views.detail, name='detail'),
    path('blog_form/',views.blog_form, name='blog_form'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>',views.edit_blog, name='edit_blog'),
]
