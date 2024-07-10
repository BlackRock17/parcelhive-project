from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from mouse_tracker import routing as mouse_tracker_routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mouse_tracker_routing.websocket_urlpatterns
        )
    ),
})