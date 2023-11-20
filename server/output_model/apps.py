from django.apps import AppConfig
from joblib import load
import os

class OutputModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'output_model'

    model_path = './output_model/files/output_model.joblib'
    model = None

    sc_X_path = './output_model/files/sc_X.joblib'
    sc_X = None
    
    sc_y_path = './output_model/files/sc_y.joblib'
    sc_y = None



    def ready(self):
        if os.path.exists(self.model_path):
            self.model = load(self.model_path)
        if os.path.exists(self.sc_X_path):
            self.sc_X = load(self.sc_X_path)
        if os.path.exists(self.sc_y_path):
            self.sc_y = load(self.sc_y_path)
        