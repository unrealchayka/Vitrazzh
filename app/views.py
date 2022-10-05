from django.shortcuts import redirect, render
from django.views import View
from .forms import TelegramMessageForm
from config import settings

import requests
import pywhatkit


token = settings.TELEGRAM_TOKEN
chat_id = settings.CHAT_ID
phone = settings.PHONE


class HomeView(View):
    def get(self, request):
        TForm = TelegramMessageForm
        return render(request, 'home.html', locals())



class TelegramView(View):
    def post(sefl, request):
        url = "https://api.telegram.org/bot" + token + "/sendMessage"
        name = request.POST['name']
        phone = request.POST['phone']
        form = TelegramMessageForm(request.POST)
        if form.is_valid():
            requests.post(url, data={
                "chat_id": '1149858211',
                "text": f'{name} {phone}'})
        return redirect('home')


class WhatsAppView(View):
    
    def get(self, request):
        message = 'Здравствуйте, мне бы хотелось сделать у вас заказ:)'
        pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=message)
        return redirect('home')
