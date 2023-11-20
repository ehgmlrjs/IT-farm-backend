from django.apps import AppConfig
from joblib import load
import os

class ReviewModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review_model'

    model_path = './review_model/files/review_model.joblib'
    model = None
    
    def ready(self):
        if os.path.exists(self.model_path):
            self.model = load(self.model_path)