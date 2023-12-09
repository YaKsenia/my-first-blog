from django.urls import path
from . import views
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from .views import MurichPageView
from .views import AraPageView
from .views import PostDetailView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('', HomePageView.as_view(), name='home'),
    path('murich', MurichPageView.as_view(), name='murich'),
    path('aryan', AraPageView.as_view(), name='aryan'),
    path('practice', views.practice, name='practice'),
    path('theory', views.theory, name='theory'),
    path('about', views.about, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_images/<int:pk>/', views.post_images, name='post_images'),
    path('post_images/<slug:slug>/', views.post_images, name='post_images'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^editor/$', TemplateView.as_view(template_name="editor.html"), name='editor'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),


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