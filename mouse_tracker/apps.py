from django.apps import AppConfig


class MouseTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mouse_tracker'

    def ready(self):
        import mouse_tracker.models
