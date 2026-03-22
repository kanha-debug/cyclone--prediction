from django.apps import AppConfig

class PredictorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predictor"

    def ready(self):
        from .utils import load_files
        model, scaler = load_files()

        # store globally
        import predictor
        predictor.model = model
        predictor.scaler = scaler