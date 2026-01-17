import requests
from bs4 import BeautifulSoup
import os
import subprocess
from telegram import Bot

URL = "https://cartoony.net/watch/sp/787/9049551"

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def get_latest_episode():
    r = requests.get(URL, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find("h1").text.strip()
    return title

def main():
    last = ""
    if os.path.exists("last.txt"):
        last = open("last.txt").read()

    latest = get_latest_episode()

    if latest != last:
        bot.send_message(chat_id=CHAT_ID, text=f"🎉 حلقة جديدة نزلت:\n{latest}")
        open("last.txt","w").write(latest)

if __name__ == "__main__":
    main()
