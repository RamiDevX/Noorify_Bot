<div align="center">
 
![NoorifyBot Banner](https://capsule-render.vercel.app/api?type=waving&color=0:001a33,20:003d66,50:0066cc,75:0088ff,100:00B4D8&height=280&section=header&text=🌙%20NoorifyBot&fontSize=80&fontColor=ffffff&fontAlignY=45&desc=📱%20Islamic%20Daily%20Reminder%20Bot&descSize=22&descAlignY=65&descColor=ffffff&animation=fadeIn)
 
[![Telegram Bot](https://img.shields.io/badge/Telegram-@Noorify__bot-0088cc?style=flat-square&logo=telegram)](https://t.me/Noorify_bot)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-00C896?style=flat-square&logo=opensourceinitiative)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

## 🌙 نبذة عن المشروع

بوت تيليغرام ذكي يرسل تذكيرات إسلامية يومية (آيات قرآنية، أدعية، أحاديث) بجدولة تلقائية دقيقة. يعمل في الدردشات الخاصة والمجموعات والقنوات مع تحكم كامل من قبل المستخدم.

---

## ✨ المميزات الأساسية

| الميزة | الوصف |
|:---:|:---|
| 🔔 **تذكيرات عشوائية** | آيات وأدعية وأحاديث غير متكررة يومياً |
| ⏰ **جدولة ذكية** | تعمل تلقائياً في أوقات محددة بدقة |
| 💬 **دعم شامل** | دردشات خاصة، مجموعات، قنوات |
| 🎛️ **تحكم سهل** | أزرار بسيطة للتحكم الكامل |
| 🔄 **بدون تكرار** | خوارزمية ذكية تمنع تكرار المحتوى |
| 📊 **قاعدة بيانات** | تخزين آمن للبيانات |

---

## 🏗️ البنية التقنية

```mermaid
flowchart TD
    A([👤 المستخدم]) -->|/start| B[💾 التسجيل]
    B --> C[⏰ تفعيل الجدولة]
    C --> D{🎲 اختيار عشوائي}
    D -->|📖| E[آية قرآنية]
    D -->|🤲| F[دعاء/ذكر]
    D -->|📿| G[حديث شريف]
    E & F & G --> H([📨 الإرسال])
    H --> I{نشط؟}
    I -->|✅| C
    I -->|/stop| J([🔴 متوقف])
```

---

## 🛠️ التقنيات المستخدمة

| التقنية | الإصدار | الدور |
|:---|:---:|:---|
| **Aiogram** | 3.x | إطار عمل بوتات Telegram |
| **APScheduler** | 3.x | جدولة المهام والتذكيرات |
| **AsyncIO** | Built-in | معالجة غير متزامنة |
| **SQLite** | 3.x | قاعدة البيانات |
| **Python** | 3.11+ | لغة البرمجة |

---

## 🚀 البدء السريع

### المتطلبات
- Python 3.11+
- pip
- Bot Token من [@BotFather](https://t.me/BotFather)

### التثبيت

```bash
# استنساخ المشروع
git clone https://github.com/RamiDevX/Noorify_Bot.git
cd Noorify_Bot

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Linux/macOS
# أو
venv\Scripts\activate  # Windows

# تثبيت المكتبات
pip install -r requirements.txt
```

### إعداد `.env`

```env
TOKEN="YOUR_BOT_TOKEN_HERE"
DATABASE_URL="sqlite:///noorify.db"
ADMIN_ID=123456789
TIMEZONE="Asia/Riyadh"
INTERVAL_MIN=60
```

### التشغيل

```bash
python main.py
```

---

## 📖 أوامر البوت الأساسية

| الأمر | الوصف |
|:---|:---|
| `/start` | تفعيل التذكيرات |
| `/stop` | إيقاف التذكيرات |
| `/resume` | استئناف التذكيرات |
| `/status` | عرض الحالة الحالية |
| `/help` | عرض قائمة الأوامر |

---

## 🤝 المساهمة

```bash
# Fork المشروع
git clone https://github.com/YOUR_USERNAME/Noorify_Bot.git

# إنشاء فرع جديد
git checkout -b feature/ميزة-جديدة

# احفظ التغييرات
git commit -m "✨ feat: إضافة ميزة جديدة"

# ادفع إلى GitHub
git push origin feature/ميزة-جديدة

# افتح Pull Request
```

---

## 👨‍💻 المطور

<div align="center">

**Rami Bitar** — RamiDevX

[![GitHub](https://img.shields.io/badge/GitHub-RamiDevX-161b22?style=flat-square&logo=github)](https://github.com/RamiDevX)
[![Telegram](https://img.shields.io/badge/Telegram-@ramidevx-0088cc?style=flat-square&logo=telegram)](https://t.me/ramidevx)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rami%20Bitar-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/ramibitar)

</div>

---

## 📚 مصادر مفيدة

- [📖 Aiogram Documentation](https://docs.aiogram.dev/)
- [⏰ APScheduler Documentation](https://apscheduler.readthedocs.io/)
- [🤖 Telegram Bot API](https://core.telegram.org/bots/api)
- [⚡ Python AsyncIO](https://docs.python.org/3/library/asyncio.html)

---

## 📜 الترخيص

مرخص تحت [MIT License](LICENSE) - استخدم وعدّل بحرية ✨

---

<div align="center">

![Views](https://komarev.com/ghpvc/?username=RamiDevX&color=006494&style=flat-square)

**صُنع بإخلاص ❤️** | NoorifyBot © 2026

⭐ *إذا أعجبك المشروع، أضف نجمة لتشجيع التطوير*

</div>
