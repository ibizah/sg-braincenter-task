"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from braincenter.views import SeriesDetailView, CreateOrUpdateSeriesView, GetSeriesDetailsView, GetSeriesCountView

# router = routers.DefaultRouter()
# router.register(r'series', SeriesListView, basename='Series' )
# router.register(r'details', SeriesDetailView, basename='Details' )
# router.register(r'taskiv', TaskFourListView )
# router.register(r'taskv', SeriesDetailView )

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('series/', CreateOrUpdateSeriesView.as_view()),
    path('series/<int:pk>/', SeriesDetailView.as_view()),
    path('series/taskiv/', GetSeriesDetailsView.as_view()),
    path('series/taskv/', GetSeriesCountView.as_view()),
]

