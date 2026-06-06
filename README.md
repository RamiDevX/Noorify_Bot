<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:051923,50:003554,100:006494&height=220&section=header&text=NoorifyBot&fontSize=72&fontColor=61B3D4&fontAlignY=42&fontAlign=50" alt="Header"/>
</p>

<div align="center">

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-0088cc?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Noorify_bot)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-006494?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/RamiDevX/Noorify_Bot?style=flat-square&logo=github&color=006494)](https://github.com/RamiDevX/Noorify_Bot)
[![Repository Size](https://img.shields.io/github/repo-size/RamiDevX/Noorify_Bot?style=flat-square&logo=github&color=006494)](https://github.com/RamiDevX/Noorify_Bot)

</div>

---

<div dir="rtl">

## 📌 نبذة عن المشروع

> *"في عالم مثقل بالإشعارات الفارغة — هذا هو الإشعار الوحيد الذي يستحق أن تفتحه."*

**نورفاي** بوت ذكي يرسل لك تذكيرات إسلامية جميلة يومياً، يحول هاتفك والمجموعات من التشتت إلى واحات عامرة بالذكر والأذكار التفاعلية.

### 🎯 الرسالة
نشر الذكر والأدعية والآيات القرآنية بطريقة منظمة وتفاعلية لكل مستخدم.

---

## ✨ المميزات الرئيسية

| 🎯 الميزة | 📝 الوصف |
|:---:|:---|
| 🔔 **تذكيرات عشوائية** | آيات وأدعية وأحاديث غير متكررة كل يوم |
| ⏱️ **جدولة ذكية** | تعمل تلقائياً في أوقات محددة |
| 💬 **دعم شامل** | دردشات خاصة، مجموعات، وقنوات |
| 🎛️ **واجهة سهلة** | أزرار بسيطة وواضحة للتحكم |
| ⚙️ **تحكم كامل** | ابدأ، توقف، أو غيّر الإعدادات في أي وقت |
| 📊 **قاعدة بيانات** | تخزين آمن وخفيف للبيانات |

---

## 🛠️ التقنيات المستخدمة

<div align="center">

| التقنية | الوصف | الإصدار |
|:---:|:---|:---:|
| 🤖 **Aiogram** | إطار عمل بوتات التيليغرام | 3.x |
| ⏰ **APScheduler** | جدولة المهام والتذكيرات | 3.x |
| ⚡ **AsyncIO** | معالجة غير متزامنة | Built-in |
| 🗄️ **SQLite** | قاعدة البيانات | 3.x |

</div>

---

## 🚀 البدء السريع

### المتطلبات الأساسية
- Python 3.11 أو أحدث
- pip (مدير المكتبات)
- رمز (Token) من BotFather على Telegram

### 1️⃣ التثبيت والإعداد

```bash
# استنساخ المشروع
git clone https://github.com/RamiDevX/Noorify_Bot.git
cd Noorify_Bot

# إنشاء بيئة افتراضية (اختياري لكن موصى به)
python -m venv venv
source venv/bin/activate  # على Windows: venv\Scripts\activate

# تثبيت المكتبات المطلوبة
pip install -r requirements.txt
```

### 2️⃣ إعداد متغيرات البيئة

أنشئ ملف `.env` في جذر المشروع:

```env
# ⚠️ مطلوب - استخدم توكن بوتك من BotFather
TOKEN="YOUR_BOT_TOKEN_HERE"

# 📍 اختياري - الإعدادات الإضافية
DATABASE_URL="sqlite:///noorify.db"
ADMIN_ID=123456789
TIMEZONE="Asia/Riyadh"
INTERVAL_MIN=60
```

### 3️⃣ كيفية الحصول على التوكن

1. افتح **[@BotFather](https://t.me/BotFather)** على Telegram
2. أرسل الأمر `/newbot`
3. اتبع التعليمات (اختر اسم وusername للبوت)
4. ستحصل على **TOKEN** - انسخه في ملف `.env`

### 4️⃣ تشغيل البوت

```bash
python bot.py
```

> ✅ متوافق مع: **Linux** | **Windows** | **macOS**

---

## 📁 هيكل المشروع

```
Noorify_Bot/
├── 📄 bot.py                    # نقطة البداية الرئيسية
├── 📄 requirements.txt           # المكتبات المطلوبة
├── 📄 .env.example              # قالب للإعدادات
├── 📄 Procfile                  # إعدادات النشر (Railway/Heroku)
├── 📄 README.md                 # التوثيق
├── 📄 LICENSE                   # رخصة المشروع (MIT)
│
├── 📁 handlers/                 # معالجات الأوامر والرسائل
│   ├── __init__.py
│   ├── commands.py              # أوامر البوت الأساسية
│   └── callbacks.py             # معالجات الأزرار
│
├── 📁 database/                 # إدارة قاعدة البيانات
│   └── db_handler.py
│
├── 📁 data/                     # بيانات الآيات والأدعية والأحاديث
│   ├── quran.json
│   ├── duas.json
│   └── hadiths.json
│
└── 📁 utils/                    # دوال مساعدة
    ├── scheduler.py             # جدولة المهام
    └── config.py                # الإعدادات

```

---

## 📋 أوامر البوت

| الأمر | الوصف | الاستخدام |
|:---:|:---|:---|
| `/start` | بدء استخدام البوت | `/start` |
| `/help` | عرض المساعدة | `/help` |
| `/stop` | إيقاف التذكيرات | `/stop` |
| `/resume` | استئناف التذكيرات | `/resume` |
| `/settings` | إدارة الإعدادات | `/settings` |
| `/about` | معلومات عن البوت | `/about` |

---

## 🌐 الروابط والتواصل

<div align="center">

### 🔗 تابعني على المنصات المختلفة

| 🤖 البوت | 💬 Telegram | 🐙 GitHub | 🔗 Linktree |
|:---:|:---:|:---:|:---:|
| [@Noorify_bot](https://t.me/Noorify_bot) | [@ramibitar](https://t.me/ramibitar) | [RamiDevX](https://github.com/RamiDevX) | [ramibitar](https://linktr.ee/ramibitar) |

### 💡 الدعم والمساعدة

| 🐛 إبلاغ عن مشكلة | 💬 تواصل مباشر |
|:---:|:---:|
| [فتح Issue](https://github.com/RamiDevX/Noorify_Bot/issues) | [راسلني على Telegram](https://t.me/ramibitar) |

</div>

---

## 📝 المساهمة والتطوير

نرحب بمساهماتك! إذا كان لديك اقتراح أو وجدت مشكلة:

1. **Fork** المشروع
2. أنشئ **Branch** للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. **Commit** تغييراتك (`git commit -m 'Add AmazingFeature'`)
4. **Push** إلى الـ Branch (`git push origin feature/AmazingFeature`)
5. افتح **Pull Request**

---

## 👨‍💻 المطور

<div align="center">

**Rami Bitar** | RamiDevX

[![GitHub](https://img.shields.io/badge/GitHub-RamiDevX-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiDevX)
&nbsp;
[![Telegram](https://img.shields.io/badge/Telegram-@ramibitar-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ramibitar)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rami%20Bitar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ramibitar)

</div>

---

## 📜 الترخيص

هذا المشروع مرخص تحت **[MIT License](LICENSE)** — يمكنك استخدامه وتعديله وتوزيعه بحرية! ✨

```
MIT License

Copyright (c) 2025 Rami Bitar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🎓 مصادر مفيدة

- 📚 [Aiogram Documentation](https://docs.aiogram.dev/)
- ⏰ [APScheduler Documentation](https://apscheduler.readthedocs.io/)
- 🤖 [Telegram Bot API](https://core.telegram.org/bots/api)
- 🐍 [Python AsyncIO](https://docs.python.org/3/library/asyncio.html)
- 🗄️ [SQLite Documentation](https://www.sqlite.org/docs.html)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:006494,50:003554,100:051923&height=140&section=footer" alt="Footer"/>
</p>

<p align="center">
  <sub>صُنع بنية وإخلاص ❤️</sub>
</p>

<p align="center">
  <sub>🌙 NoorifyBot © 2025 · مفتوح المصدر · في خدمة الذكر والتذكير</sub>
</p>

<p align="center">
  <sub>⭐ إذا أعجبك المشروع، أضف نجمة ⭐</sub>
</p>

</div>
