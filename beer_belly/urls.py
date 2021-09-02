from django.urls import path
from .views import BeerList, BeerDetails, BeerAdd, BeerDelete, BeerUpdate

urlpatterns = [
    path('', BeerList.as_view(), name='lists'),
    path('new/', BeerAdd.as_view(), name='add'),
    path('<int:pk>', BeerDetails.as_view(), name='details'),
    path('<int:pk>/edit', BeerUpdate.as_view(), name='updates'),
    path('<int:pk/delete', BeerDelete.as_view(), name='delete'),
]