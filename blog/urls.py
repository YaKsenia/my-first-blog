from django.urls import path
from . import views
from django.conf.urls import include, url




# posts/urls.py

#from .views import HomePageView
from .views import MurichPageView
from .views import AraPageView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('', HomePageView.as_view(), name='home'),
    path('murich', MurichPageView.as_view(), name='murich'),
    path('aryan', AraPageView.as_view(), name='aryan'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]


'''
path('admin/blog/murich', MurichPageView.as_view(), name='admin/blog/murich')
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