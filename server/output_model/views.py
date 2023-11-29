import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps

class OutputPredView(APIView):

    def post(self, request):

        app_config = apps.get_app_config('output_model')

        if app_config.ready:
            output_model = app_config.model
            scaler_X = app_config.scaler_X
            scaler_y = app_config.scaler_y
        else :
            print('여기')

        if not output_model:
            print('a')
            return Response({'error': 'model 로드 불가'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        output_data = {
            'area': request.data.get('area'),
            'humi': request.data.get('humi'),
            'temp': request.data.get('temp'),
            'earth': request.data.get('earth'),
            'radio': request.data.get('radio')
        }

        output_data = list(output_data.values())

        output_data = np.array(output_data)

        output_data_scaled = scaler_X.transform([output_data])


        # return Response(output_data_scaled)
    
        # output_data_scaled = scaler_X.transform(output_data)

        output_data_scaled = output_data_scaled.reshape((1, 1, len(output_data)))

        predicted_output_scaled = output_model.predict(output_data_scaled)

        predicted_output = scaler_y.inverse_transform(predicted_output_scaled)

        output = predicted_output[0][0].round(3)
        return Response({'output': output}, status=status.HTTP_200_OK)


