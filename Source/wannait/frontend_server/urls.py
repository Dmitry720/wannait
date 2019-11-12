from django.urls import path
from .views import RecommendationsView
from .views import OwnedProductsView
from .views import ProductInfoView
from .views import AnonymousProductInfoView
from .views import RegisteredProductInfoView
from .views import OwnerProductInfoView


app_name = 'wannait'


urlpatterns = [
    path('', RecommendationsView.as_view(), name='index')
]
