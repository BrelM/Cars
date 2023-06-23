from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.VisitorView.as_view()),
    path('login', views.login),
    path('search', views.VisitorSearchView.as_view()),
    
    #path('?pk=<int:pk>/', views.VisitorView.as_view()),
    #path('?pk=<int:pk>/<str:carModel>/<str:color>/<int:state>/<str:builder>/<str:type>/<str:date>/<str:price>/<str:orderby>/', views.VisitorView.as_view()),
]
