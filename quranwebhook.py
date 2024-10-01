import random
import requests
from bs4 import BeautifulSoup
import schedule
import time

# حط الويبهوك الخاص فيك
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID"

# تحديد آية من موقع قرآن جامعة الملك سعود
def get_random_ayah():
    url = "https://quran.ksu.edu.sa/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        return get_random_ayah
    else:
        return "لم يتم العثور على آية"

def send_to_discord(ayah):
    data = {
        "content": ayah
    }
    result = requests.post(DISCORD_WEBHOOK_URL, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
    else:
        print(f"Successfully sent: {result.status_code}")

# الدالة اللي راح تنفذ المهمة كل 12 ساعة
def job():
    ayah = get_random_ayah()
    send_to_discord(ayah)

schedule.every(12).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



#Created by : Saad Almalki , مسموح بإعادة استخدامه للأجر