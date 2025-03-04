# saltandearthbe/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from saltandearthapp.views import CityView, UserView, LodgingView, RestaurantView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cities', CityView, 'city')
router.register(r'users', UserView, 'user')
router.register(r'lodging', LodgingView, 'lodging')
router.register(r'restaurants', RestaurantView, 'restaurant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include router-generated URLs
]
