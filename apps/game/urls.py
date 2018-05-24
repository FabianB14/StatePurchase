from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.map),
    url(r'^state/([a-z]+)$', views.state),
    url(r'^restart$', views.restart),
    url(r'^turn$', views.turn),
    url(r'^data/buildings/(\d+)$', views.getBuildingData),
    url(r'^fix/buildings/(\d+)$', views.fixBuilding),
    url(r'^modify/states/(\d+)/build/([a-z]+)$', views.buyBuilding),
    url(r'^modify/states/(\d+)/improve/([a-z]+)$', views.improveTech),
]
