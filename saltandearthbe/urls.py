from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from saltandearthapp.views import CityView, UserView, LodgingView, RestaurantView, TagView, LodgingTagView, RestaurantTagView

router = routers.DefaultRouter(trailing_slash=False)  # Adding trailing_slash=False here
router.register(r'cities', CityView, 'city')
router.register(r'users', UserView, 'user')
router.register(r'lodging', LodgingView, 'lodging')
router.register(r'restaurants', RestaurantView, 'restaurant')
router.register(r'tags', TagView, 'tag')
router.register(r'restauranttags', RestaurantTagView, 'restauranttag')
router.register(r'lodgingtags', LodgingTagView, 'lodgingtag')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include router-generated URLs
]
