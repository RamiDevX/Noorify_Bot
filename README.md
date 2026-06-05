<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:051923,50:003554,100:006494&height=220&section=header&text=NoorifyBot&fontSize=72&fontColor=61B3D4&fontAlignY=42&fontAlign=50" alt="NoorifyBot Header"/>
</p>

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-Bot-0088cc?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Noorify_bot)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-006494?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/RamiDevX/Noorify_Bot?style=flat-square&logo=github&color=006494)](https://github.com/RamiDevX/Noorify_Bot)

</div>

---

<div dir="rtl">

## 📌 عن المشروع

> *"في عالم مثقل بالإشعارات الفارغة — هذا هو الإشعار الوحيد الذي يستحق أن تفتحه."*

**NoorifyBot** هو بوت تيليغرام ذكي يرسل لك تذكيرات إسلامية جميلة كل يوم:
- 📖 آيات قرآنية كريمة
- 🤲 أدعية مختارة بعناية
- 💭 أحاديث شريفة نبوية

البوت مبني بـ **Python** بطريقة غير متزامنة (Async)، خفيف الوزن، وسهل التشغيل والاستضافة.

---

## ✨ المميزات الرئيسية

| الميزة | الوصف |
|--------|-------|
| 🔔 **تذكيرات عشوائية** | لا تتكرر، تنوع روحي حقيقي كل يوم |
| ⏱️ **جدولة ذكية** | تعمل تلقائياً في أوقات محددة |
| 💬 **دعم المجموعات** | دردشات خاصة، مجموعات، وقنوات |
| 🎛️ **أزرار سهلة** | واجهة بسيطة وواضحة للتحكم |
| ⚙️ **تحكم كامل** | ابدأ، توقف، أو غيّر الإعدادات في أي وقت |

---

## 🛠️ التقنيات المستخدمة

| التقنية | الإصدار | الفائدة |
|---------|---------|---------|
| **Aiogram** | 3.x | إطار عمل قوي لبوتات التيليغرام |
| **APScheduler** | 3.x | جدولة المهام والتذكيرات |
| **Asyncio** | مدمج | معالجة سريعة وفعالة |
| **SQLite** | — | حفظ البيانات بأمان |

---

## 🚀 البدء السريع

### 1️⃣ التثبيت

```bash
# نسخ المشروع
git clone https://github.com/RamiDevX/Noorify_Bot.git
cd Noorify_Bot

# تثبيت المكتبات
pip install -r requirements.txt

# تشغيل البوت
python bot.py
```

> متوافق مع: Linux ✓ | Windows ✓ | macOS ✓

### 2️⃣ الإعدادات

أنشئ ملف `.env` في المشروع بهذا الشكل:

```env
# مطلوب - استخدم توكن بوتك
TOKEN="YOUR_BOT_TOKEN_HERE"

# اختياري
DATABASE_URL="sqlite:///noorify.db"
ADMIN_ID=123456789
TIMEZONE="Asia/Riyadh"
INTERVAL_MIN=60
```

### 3️⃣ كيفية الحصول على التوكن

1. افتح [@BotFather](https://t.me/BotFather)
2. اكتب `/newbot`
3. اتبع التعليمات واحصل على التوكن
4. ضع التوكن في ملف `.env`

---

## 📁 هيكل المشروع

```
Noorify_Bot/
├── bot.py                 # نقطة البداية الرئيسية
├── requirements.txt       # المكتبات المطلوبة
├── .env.example          # قالب للإعدادات
├── Procfile              # لنشر البوت على Railway
├── README.md             # هذا الملف
├── LICENSE               # رخصة المشروع
└── handlers/             # معالجات أوامر البوت
```

---

## 🔗 الروابط المهمة

<div align="center">

| الرابط | النوع |
|--------|-------|
| [@Noorify_bot](https://t.me/Noorify_bot) | 🤖 البوت |
| [@ramibitar](https://t.me/ramibitar) | 💬 التيليغرام |
| [GitHub](https://github.com/RamiDevX/Noorify_Bot) | 🐙 المستودع |
| [روابطي](https://linktr.ee/ramibitar) | 🔗 جميع الروابط |

</div>

---

## 👨‍💻 المطور

<div align="center">

<img src="https://github.com/RamiDevX.png" width="80" style="border-radius:50%"/>

**رامي بيطار**

[GitHub](https://github.com/RamiDevX) · [Telegram](https://t.me/ramibitar)

</div>

---

## 💡 المساعدة والدعم

هل واجهت مشكلة؟

- 🐛 **إبلاغ عن خطأ**: [أنشئ Issue](https://github.com/RamiDevX/Noorify_Bot/issues)
[ramibitar](https://t.me/ramibitar)---
---

## 📜 الترخيص

هذا المشروع مرخص تحت [MIT License](LICENSE) — يمكنك استخدامه بحرية! ✨

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:006494,50:003554,100:051923&height=140&section=footer" alt="Footer"/>
</p>

<p align="center">
  <sub>✨ صُنع بنية وإخلاص ✨</sub>
</p>

<p align="center">
  <sub>🌙 NoorifyBot © 2026 · مفتوح المصدر · في خدمة الذكر والتذكير</sub>
</p>

<p align="center">
  <sub>⭐ إذا أعجبك المشروع، أضف نجمة ⭐</sub>
</p>

</div>
