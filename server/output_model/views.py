from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.apps import apps
import numpy as np
from sklearn.preprocessing import StandardScaler

class OutputPredView(APIView):
    def post(self, request):
        app_config = apps.get_app_config('output_model')
        print(app_config)

        output_model = app_config.model
        sc_X = app_config.sc_X
        sc_y = app_config.sc_y

        print(output_model)
        if not output_model:
            return Response({'error': 'model 로드 불가'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        output_data = {
            'humi': request.data.get('humi'),
            'temp': request.data.get('temp'),
            'earth': request.data.get('earth'),
            'radio': request.data.get('radio')
        }

        output_data = list(output_data.values())

        real_data = np.array([output_data])

        real_data_scaled = sc_X.transform(real_data)

        real_data_pred = output_model.predict(real_data_scaled)

        real_data_pred_original_scale = sc_y.inverse_transform(real_data_pred.reshape(-1, 1))
        
        output = real_data_pred_original_scale[0][0].round(3)
        return Response({'output': output}, status=status.HTTP_200_OK)