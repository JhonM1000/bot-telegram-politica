import requests
import time
from telegram import Bot

TOKEN = "
8617007872:AAFkpvHES7F2KSdgvx6kbHA5g_EGMmU9bFU"
CHAT_ID = "@Politica24H"
API_KEY = "86f017284e7b4ca389537cc1fd7b3932"

bot = Bot(token=TOKEN)
enviadas = set()

def noticias():
    url = f"https://newsapi.org/v2/top-headlines?country=br&q=politica&apiKey={API_KEY}"
    r = requests.get(url).json()
    return r.get("articles", [])

def enviar(titulo, link):
    msg = f"🚨 POLÍTICA AGORA\n\n{titulo}\n\nLeia: {link}"
    bot.send_message(chat_id=CHAT_ID, text=msg)

while True:
    try:
        for n in noticias():
            t = n["title"]
            l = n["url"]

            if t not in enviadas:
                enviar(t, l)
                enviadas.add(t)
                time.sleep(15)
    except Exception as e:
        print(e)

    time.sleep(600)
