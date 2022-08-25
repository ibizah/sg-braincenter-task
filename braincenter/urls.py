from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('series/', views.CreateOrUpdateSeriesView().as_view()),
    path('series/<int:pk>/', views.SeriesDetailView.as_view()),
    path('queries/', views.TaskfourListView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)