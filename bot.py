import requests
import asyncio
from telegram import Bot

TOKEN = "SEU_TOKEN"
CHAT_ID = -1003849395765
API_KEY = "SUA_API_KEY"

bot = Bot(token=TOKEN)
enviadas = set()

def noticias():
    url = f"https://newsapi.org/v2/everything?q=política&language=pt&sortBy=publishedAt&apiKey={API_KEY}"

    print("Buscando notícias...")

    r = requests.get(url)
    print("Status API:", r.status_code)

    data = r.json()

    artigos = data.get("articles", [])

    print("Quantidade de notícias:", len(artigos))

    return artigos

async def enviar(titulo, link):
    msg = f"🚨 POLÍTICA AGORA\n\n{titulo}\n\nLeia: {link}"

    print("Enviando:", titulo)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=msg
    )

async def main():
    while True:
        try:
            artigos = noticias()

            # pega apenas 3 notícias por ciclo
            for n in artigos[:3]:

                t = n["title"]
                l = n["url"]

                if t not in enviadas:

                    await enviar(t, l)

                    enviadas.add(t)

                    print("Notícia enviada")

                    # espera 30 minutos
                    await asyncio.sleep(900)

        except Exception as e:
            print("ERRO:", e)

        print("Aguardando próximo ciclo...")

        # verifica novas notícias a cada 10 minutos
        await asyncio.sleep(600)

asyncio.run(main())
