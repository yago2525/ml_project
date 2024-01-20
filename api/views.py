from rest_framework import generics
from api.apps import ApiConfig
from rest_framework.response import Response
from .serializers import HousePricePredictSerializer
import numpy as np

class HousePricePredict(generics.CreateAPIView):
    serializer_class = HousePricePredictSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        zn = serializer.validated_data.get('zn')
        rm = serializer.validated_data.get('rm')
        dis = serializer.validated_data.get('dis')
        chas = serializer.validated_data.get('chas')

        pred_model = ApiConfig.model
        prediction = pred_model.predict([[zn, rm, dis, chas]])
        prediction = np.round(prediction)[0][0]

        response_data = {
            f"Predicted price": prediction
        }
        return Response(response_data, status=200)
