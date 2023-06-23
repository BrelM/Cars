from django.urls import path
from .views import *

from visitor.views import VisitorSearchView

urlpatterns = [
    path('users', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    
    # Create, update, delete class-based view
    path('', UserAnnouncementView.as_view()),
    
    path('search', VisitorSearchView.as_view()),

    path('me', MyAnnouncementView.as_view()),

    # Forms elements
    path('cartypes/', CarTypeView.as_view()),
    path('builders/', BuilderView.as_view()),
    path('enginetypes/', EngineTypeView.as_view()),
    path('carburants/', CarburantView.as_view()),
    path('powertypes/', PowerTypeView.as_view()),
    path('speedtypes/', SpeedTypeView.as_view()),

    #path('?pk=<int:pk>/', views.VisitorView.as_view()),
    #path('?pk=<int:pk>/<str:carModel>/<str:color>/<int:state>/<str:builder>/<str:type>/<str:date>/<str:price>/<str:orderby>/', views.VisitorView.as_view()),
]
