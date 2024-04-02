from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        import app.signals

# class YourAppNameConfig(AppConfig):
#     name = 'your_app_name'

#     def ready(self):
#         import your_app_name.signals