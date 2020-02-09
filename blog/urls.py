from django.urls import path
from . import views


# posts/urls.py

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]


'''
urlpatterns = [
    path('', views.post_list),
    path('post/', views.post_detail),
    path('post/new/', views.post_new),
    path('post/edit/', views.post_edit),

]

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
'''