from django.apps import AppConfig
from joblib import load
from tensorflow.keras.models import load_model
import os

class OutputModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'output_model'

    model_path = './output_model/files/output_model.h5'
    model = None

    scaler_X_path = './output_model/files/scaler_X.joblib'
    scaler_X = None

    scaler_y_path = './output_model/files/scaler_y.joblib'
    scaler_y = None

    def ready(self):
        if os.path.exists(self.model_path):
            self.model = load_model(self.model_path)
        if os.path.exists(self.scaler_X_path):
            self.scaler_X = load(self.scaler_X_path)
        if os.path.exists(self.scaler_y_path):
            self.scaler_y = load(self.scaler_y_path)
