# 🌙 NoorifyBot

<div align="center">

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Noorify_bot)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-006494?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/RamiDevX/Noorify_Bot?style=for-the-badge&logo=github)](https://github.com/RamiDevX/Noorify_Bot)

**بوت ذكي يرسل تذكيرات إسلامية يومية جميلة 🕌 | تحويل هاتفك إلى واحة عامرة بالذكر والأدعية**

</div>

---

## 📌 نبذة عن المشروع

> *"في عالم مثقل بالإشعارات الفارغة — هذا هو الإشعار الوحيد الذي يستحق أن تفتحه."*

**NoorifyBot** هو بوت ذكي يومي يرسل لك:
- 🕌 **آيات قرآنية** مختارة بعناية
- 📖 **أحاديث نبوية** صحيحة
- 💫 **أدعية وأذكار** مميزة
- ✨ **محتوى إسلامي** متنوع

**رسالتنا:** نشر الذكر والأدعية بطريقة منظمة وتفاعلية وسهلة الاستخدام.

---

## ✨ المميزات الرئيسية

<table>
  <tr>
    <td align="center"><strong>🔔 تذكيرات يومية</strong><br/>آيات وأدعية غير متكررة</td>
    <td align="center"><strong>⏱️ جدولة ذكية</strong><br/>تعمل تلقائياً في أوقات محددة</td>
    <td align="center"><strong>💬 دعم شامل</strong><br/>دردشات خاصة ومجموعات وقنوات</td>
  </tr>
  <tr>
    <td align="center"><strong>🎛️ واجهة سهلة</strong><br/>أزرار واضحة وبسيطة</td>
    <td align="center"><strong>⚙️ تحكم كامل</strong><br/>ابدأ، توقف، أو غيّر الإعدادات</td>
    <td align="center"><strong>📊 قاعدة آمنة</strong><br/>تخزين خفيف وآمن للبيانات</td>
  </tr>
</table>

---

## 🛠️ التقنيات والأدوات

<div align="center">

| المكتبة | الوظيفة | الإصدار |
|:---:|:---|:---:|
| **Aiogram** | إطار عمل بوتات Telegram | 3.x |
| **APScheduler** | جدولة المهام التلقائية | 3.x |
| **AsyncIO** | معالجة غير متزامنة | Built-in |
| **SQLite** | قاعدة البيانات الخفيفة | 3.x |

</div>

---

## 🚀 البدء السريع

### المتطلبات الأساسية
- ✅ Python 3.11 أو أحدث
- ✅ pip (مدير المكتبات)
- ✅ رمز بوت Telegram (Token من BotFather)

### 1️⃣ الخطوة الأولى: الحصول على رمز البوت

```bash
1. افتح @BotFather على Telegram
2. أرسل الأمر: /newbot
3. اختر اسم البوت (مثال: NoorifyBot)
4. اختر username للبوت (مثال: Noorify_bot)
5. سيعطيك رمز البوت (Token) - احفظه في مكان آمن
```

### 2️⃣ الخطوة الثانية: تثبيت المشروع

```bash
# استنساخ المشروع من GitHub
git clone https://github.com/RamiDevX/Noorify_Bot.git
cd Noorify_Bot

# إنشاء بيئة افتراضية (اختياري لكن موصى به)
python -m venv venv

# تفعيل البيئة الافتراضية
# على Linux/macOS:
source venv/bin/activate

# على Windows:
venv\Scripts\activate

# تثبيت المكتبات المطلوبة
pip install -r requirements.txt
```

### 3️⃣ الخطوة الثالثة: إعداد متغيرات البيئة

أنشئ ملف `.env` في جذر المشروع بالمحتوى التالي:

```env
# 🔴 مطلوب - ضع رمز بوتك هنا
TOKEN="YOUR_BOT_TOKEN_HERE"

# ⚪ اختياري - معرف المسؤول
ADMIN_ID=123456789

# ⚪ اختياري - المنطقة الزمنية
TIMEZONE="Asia/Riyadh"

# ⚪ اختياري - المدة بين التذكيرات بالدقائق
INTERVAL_MIN=60

# ⚪ اختياري - رابط قاعدة البيانات
DATABASE_URL="sqlite:///noorify.db"
```

### 4️⃣ الخطوة الرابعة: تشغيل البوت

```bash
python bot.py
```

✅ **تم! البوت يعمل الآن.** افتح Telegram وابدأ استخدام البوت!

---

## 📁 هيكل المشروع

```
Noorify_Bot/
│
├── 📄 bot.py                      # 🎯 نقطة البداية الرئيسية
├── 📄 requirements.txt             # 📦 المكتبات المطلوبة
├── 📄 .env.example                # ⚙️ قالب الإعدادات
├── 📄 Procfile                    # ☁️ إعدادات النشر
├── 📄 README.md                   # 📚 هذا الملف
├── 📄 LICENSE                     # 📋 رخصة MIT
│
├── 📁 handlers/                   # 🔧 معالجات الأوامر
│   ├── __init__.py
│   ├── commands.py                # أوامر البوت الأساسية
│   └── callbacks.py               # معالجات الأزرار التفاعلية
│
├── 📁 database/                   # 🗄️ إدارة البيانات
│   └── db_handler.py              # معالج قاعدة البيانات
│
├── 📁 data/                       # 📖 البيانات الإسلامية
│   ├── quran.json                 # الآيات القرآنية
│   ├── duas.json                  # الأدعية والأذكار
│   └── hadiths.json               # الأحاديث النبوية
│
└── 📁 utils/                      # 🛠️ دوال مساعدة
    ├── scheduler.py               # جدولة المهام
    └── config.py                  # إعدادات البوت
```

---

## 📋 أوامر البوت الأساسية

| الأمر | الوصف | مثال |
|:---:|:---|:---|
| `/start` | بدء استخدام البوت 🚀 | `/start` |
| `/help` | عرض قائمة المساعدة 📚 | `/help` |
| `/stop` | إيقاف التذكيرات ⏸️ | `/stop` |
| `/resume` | استئناف التذكيرات ▶️ | `/resume` |
| `/settings` | إدارة الإعدادات ⚙️ | `/settings` |
| `/stats` | عرض الإحصائيات 📊 | `/stats` |
| `/about` | معلومات عن البوت ℹ️ | `/about` |

---

## 🎯 المميزات المتقدمة

### 🔔 نظام التذكيرات الذكي
- تذكيرات يومية في أوقات محددة
- محتوى متنوع (آيات، أدعية، أحاديث)
- عدم تكرار المحتوى

### 💾 إدارة البيانات
- حفظ آمن للبيانات
- قاعدة بيانات خفيفة SQLite
- نسخ احتياطية تلقائية

### 🌐 التوافقية الشاملة
- يعمل على الدردشات الخاصة
- يعمل على المجموعات
- يعمل على القنوات

### 📱 الاستجابة السريعة
- معالجة غير متزامنة (AsyncIO)
- استجابة فورية للأوامر
- استهلاك منخفض للموارد

---

## 🌐 روابط وتواصل

<div align="center">

### 📞 تواصل معنا
| النوع | الرابط |
|:---:|:---|
| 🤖 **البوت الرسمي** | [@Noorify_bot](https://t.me/Noorify_bot) |
| 💬 **الحساب الشخصي** | [@ramibitar](https://t.me/ramibitar) |
| 🐙 **GitHub** | [RamiDevX](https://github.com/RamiDevX) |
| 🔗 **جميع الروابط** | [Linktree](https://linktr.ee/ramibitar) |

### 🆘 الدعم والمساعدة
| المشكلة | الحل |
|:---:|:---|
| 🐛 **وجدت خطأ؟** | [فتح Issue على GitHub](https://github.com/RamiDevX/Noorify_Bot/issues) |
| 💬 **سؤال أو اقتراح؟** | [راسلني على Telegram](https://t.me/ramibitar) |

</div>

---

## 📝 المساهمة في المشروع

نحن نرحب بمساهماتك! 💝 إليك كيفية المساهمة:

### خطوات المساهمة:
```bash
# 1. عمل Fork للمشروع (زر العلوي على GitHub)

# 2. استنساخ المشروع الخاص بك
git clone https://github.com/YOUR_USERNAME/Noorify_Bot.git
cd Noorify_Bot

# 3. إنشاء فرع جديد لميزتك
git checkout -b feature/ميزتي-الرائعة

# 4. تعديل الملفات وإضافة التحسينات

# 5. حفظ التغييرات
git add .
git commit -m "إضافة: وصف تفصيلي للتحسين"

# 6. رفع التغييرات
git push origin feature/ميزتي-الرائعة

# 7. فتح Pull Request على GitHub
```

---

## 🚀 نشر البوت على السحابة

### خيار 1: Railway (موصى به)
```bash
# أنشئ حساب على https://railway.app
# ربط مشروعك على GitHub
# ضع متغيرات البيئة في Railway
```

### خيار 2: Heroku
```bash
# تثبيت Heroku CLI
# heroku login
# heroku create your-bot-name
# git push heroku main
```

### خيار 3: الخادم الشخصي
```bash
# انسخ الملفات على الخادم
# ثبت Python 3.11+
# شغل: python bot.py
```

---

## 📚 مصادر مفيدة

| الموضوع | الرابط |
|:---:|:---|
| 📖 Aiogram | [Documentation](https://docs.aiogram.dev/) |
| ⏰ APScheduler | [Documentation](https://apscheduler.readthedocs.io/) |
| 🤖 Telegram API | [API Reference](https://core.telegram.org/bots/api) |
| 🐍 Python AsyncIO | [Documentation](https://docs.python.org/3/library/asyncio.html) |
| 🗄️ SQLite | [Official Site](https://www.sqlite.org/docs.html) |

---

## ❓ الأسئلة الشائعة (FAQ)

<details>
<summary><b>❓ هل البوت مجاني؟</b></summary>

نعم! البوت مجاني تماماً ومفتوح المصدر. يمكنك تشغيله على خادمك الخاص.
</details>

<details>
<summary><b>❓ هل يتطلب رسوم للنشر على السحابة؟</b></summary>

معظم خدمات السحابة (Railway, Heroku) توفر خطة مجانية. تحقق من حدود الخطة المجانية.
</details>

<details>
<summary><b>❓ كيف أضيف محتوى إسلامي جديد؟</b></summary>

عدّل ملفات JSON في مجلد `data/` وأضف المحتوى الجديد بنفس الصيغة.
</details>

<details>
<summary><b>❓ هل يدعم اللغات الأخرى؟</b></summary>

حالياً البوت باللغة العربية. يمكن إضافة لغات أخرى من خلال المساهمة.
</details>

<details>
<summary><b>❓ كيف أبلغ عن مشكلة؟</b></summary>

افتح Issue على GitHub وصِف المشكلة بالتفصيل مع لقطات شاشة إن أمكن.
</details>

---

## 👨‍💻 المطور

<div align="center">

### **Rami Bitar** | RamiDevX

[![GitHub](https://img.shields.io/badge/GitHub-RamiDevX-161b22?style=for-the-badge&logo=github)](https://github.com/RamiDevX)
[![Telegram](https://img.shields.io/badge/Telegram-@ramibitar-0088cc?style=for-the-badge&logo=telegram)](https://t.me/ramibitar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rami%20Bitar-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ramibitar)

**مطور فلسطيني متخصص في بوتات Telegram والتطبيقات الذكية** 🇵🇸

</div>

---

## 📜 الترخيص

هذا المشروع مرخص تحت **MIT License** - يمكنك استخدامه وتعديله وتوزيعه بحرية! ✨

```
MIT License (c) 2025 Rami Bitar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
```

---

## 🌟 ادعم المشروع

<div align="center">

### هل أعجبك المشروع؟

⭐ **أضف نجمة** لدعم هذا المشروع  
🍴 **عمل Fork** للتطوير عليه  
📢 **شاركه** مع الآخرين  
💬 **أرسل اقتراحاتك** لتحسينه  

```
صُنع بنية وإخلاص ❤️
🌙 NoorifyBot © 2025
مفتوح المصدر | في خدمة الذكر والتذكير
```

</div>

---

<div align="center">

**حالة المشروع:** 🟢 نشط ومستمر في التطوير

</div>
