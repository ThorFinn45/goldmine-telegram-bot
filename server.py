from flask import Flask, request
import requests

app = Flask(__name__)

# إعدادات البوت
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"  # استبدل هذا برمز البوت من @BotFather
CHAT_ID = "YOUR_CHANNEL_ID"  # استبدل هذا بمعرف القناة (مثل -100123456789)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get('signal')
    symbol = data.get('symbol')
    price = data.get('price')
    time = data.get('time')
    stop_loss = data.get('stop_loss', 'غير محدد')
    take_profit = data.get('take_profit', 'غير محدد')

    # تنسيق الرسالة
    message = f"📊 إشارة تداول جديدة\n" \
              f"نوع الإشارة: {signal}\n" \
              f"الرمز: {symbol}\n" \
              f"السعر: {price}\n" \
              f"وقف الخسارة: {stop_loss}\n" \
              f"جني الأرباح: {take_profit}\n" \
              f"الوقت: {time}"

    # إرسال الرسالة إلى تليجرام
    url = f"https://api.telegram.org/bot7801801311:AAEE033M2x-qBcaqw5JdsGqSbHVEcEpxMdA/sendMessage"
    payload = {
        "chat_id": 5760526611,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return {"status": "success"}, 200
    else:
        return {"status": "error", "message": response.text}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
