from .views import HousePricePredict
from django.urls import path

urlpatterns = [
    path("predict/", HousePricePredict.as_view(), name="predict_price"),
]
