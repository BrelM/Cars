from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
    path('', views.VisitorView.as_view()),

    # Forms elements
    path('cartypes/', CarTypeView.as_view()),
    path('builers/', BuilderView.as_view()),
    path('enginetypes/', EngineTypeView.as_view()),
    path('caburants/', CarburantView.as_view()),
    path('powertypes/', PowerTypeView.as_view()),
    path('speedtypes/', SpeedTypeView.as_view()),

    #path('?pk=<int:pk>/', views.VisitorView.as_view()),
    #path('?pk=<int:pk>/<str:carModel>/<str:color>/<int:state>/<str:builder>/<str:type>/<str:date>/<str:price>/<str:orderby>/', views.VisitorView.as_view()),
]
