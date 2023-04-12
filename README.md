
# FastAPI Telegram Bot


- Loyihani ishga tushirish uchun NGROK ni yuklab olishingiz kerak [Ngrok](https://www.ngrok.com/)

- Ketma ketlikni bajaring:
  - Loyiha uchun kerakli paketlarni o'rnating
      ```
      pip install -r requirements.txt
      ```
      
  - Loyihani ishga tushiring:
      ```
      uvicorn main:app
      ```
      
  - Ngrok joylashgan papkaga cmd(terminal) orqli kirib oling.
      ```
      ngrok http 8000
      ```
      
  - Ngrokni ishga tushirganda  https://2c1f-84-54-92-191.eu.ngrok.io shunga yaqin url tuzib beradi.Urlni oling va main.py faylidagi WEBHOOK_URL  o'zgaruvchisiga quydagi ko'rinishda yozing
      ```
      WEBHOOK_URL= "https://2c1f-84-54-92-191.eu.ngrok.io" + WEBHOOK_PATH
      ```
      
  - Loyihani qayta ishga tushiring:
      ```
      uvicorn main:app
      ```
      
  -  Bravzer orqali __https://api.telegram.org/bot{BotTokeningizni yozing}/getwebhookinfo__ shu urlga murojaat qilib ko'ring, ngrok urlini ko'rsangiz bot ishga tushgan bo'ladi


 <hr>
 Mehnatimiz sizga foyda berayotgan bolsa GITHUB profilimizga obuna bo'ling va telegram kanalimizda reaksiyalarni qoldiring 👍
 
# *E'tiboringiz uchun rahmat* Savollaringiz bo'lsa [Telegram](https://t.me/foydamizteg_sin)
