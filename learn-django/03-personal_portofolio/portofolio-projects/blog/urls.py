from django.urls import path


from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<int:blog_title>', views.detail, name='detail')
] 
