from django.conf.urls import url
from django.conf.urls import include
from petfeeder import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework.authtoken import views as auth_views


router = routers.DefaultRouter()
router.register(r'petfeeders', views.PetFeederViewSet, 'petfeeders')
router.register(r'pets', views.PetViewSet, 'pets')
router.register(r'petfood', views.PetFoodViewSet, 'petfood')
router.register(r'fooddispenseractions', views.FoodDispenserActionViewSet, 'fooddispenseractions')
router.register(r'userrequestactions', views.UserRequestActionViewSet, 'userrequestactions')
router.register(r'petconsumptionactions', views.PetConsumptionActionViewSet, 'petconsumptionactions')

urlpatterns = router.urls

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', auth_views.obtain_auth_token),
]

