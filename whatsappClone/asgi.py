"""
ASGI config for whatsappClone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chatapp import consumers
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whatsappClone.settings")

# application = get_asgi_application()
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', consumers.PersonalChatConsumer )
        ])
    )
    
})