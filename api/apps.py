from django.apps import AppConfig
import os
from django.conf import settings
import joblib
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE=os.path.join(settings.MODELS, 'house_pred_model.joblib')
    model=joblib.load(MODEL_FILE)

