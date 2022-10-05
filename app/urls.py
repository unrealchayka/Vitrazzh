from django.urls import path
from .views import HomeView, TelegramView, WhatsAppView

urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('telegram/', TelegramView.as_view(), name = 'telegram'),
    path('whatsapp/', WhatsAppView.as_view(), name = 'whatsapp'),
]
