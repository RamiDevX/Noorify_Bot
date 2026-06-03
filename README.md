<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:051923,50:003554,100:006494&height=220&section=header&text=NoorifyBot&fontSize=72&fontColor=61B3D4&fontAlignY=42&fontAlign=50&desc=تذكيرات%20إسلامية%20ذكية%20على%20تيليغرام&descSize=18&descAlignY=65&descAlign=50&animation=fadeIn" width="100%"/>
</p>

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-Bot-0088cc?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Noorify_bot)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-006494?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/RamiAIlab/Noorify_Bot?style=flat-square&logo=github&color=006494)](https://github.com/RamiAIlab/Noorify_Bot)

</div>

---

<div dir="rtl">

## عن المشروع

> *"في عالم مثقل بالإشعارات الفارغة — هذا هو الإشعار الوحيد الذي يستحق أن تفتحه."*

بوت تيليغرام ذكي يُرسل تذكيرات إسلامية مختارة بعناية: أدعية، آيات قرآنية، وأحاديث شريفة — مجدولةً تلقائياً إلى محادثاتك الخاصة، المجموعات، والقنوات.

مبني بـ Python غير متزامن، مُجدوِل خفيف الوزن، وبصمة برمجية صغيرة — سهل الاستضافة الذاتية وقابل للتوسع.

---

## المميزات

| الميزة | التفاصيل |
|--------|----------|
| 🔔 تذكيرات عشوائية | خوارزمية ضد التكرار تضمن تنوعاً روحياً حقيقياً |
| ⏱️ جدولة دقيقة | مدعوم بـ APScheduler — اضبطه مرة واحدة وانسَهُ |
| 💬 متعدد المحادثات | دردشات خاصة، مجموعات، وقنوات — جلسة مستقلة لكل محادثة |
| 🎛️ واجهة تفاعلية | لوحة أزرار Inline نظيفة وبديهية |
| ▶️ تحكم كامل | `/start` و `/stop` — اشترك أو ألغِ في أي وقت |

---

## التقنيات

| المكتبة | الإصدار | الدور |
|---------|---------|-------|
| **Aiogram** | 3.x | إطار عمل تيليغرام غير متزامن |
| **APScheduler** | 3.x | جدولة المهام الذكية |
| **Asyncio** | مدمج | معالجة غير متزامنة |
| **SQLite** | — | تخزين البيانات خفيف وآمن |

---

## التثبيت

```bash
git clone https://github.com/RamiAIlab/Noorify_Bot.git
cd Noorify_Bot
pip install -r requirements.txt
python bot.py
```

> ✓ مختبر على  Windows
---

## الإعدادات

أنشئ ملف `.env` في جذر المشروع:

```env
# مطلوب
TOKEN="YOUR_BOT_TOKEN_HERE"

# اختياري
# DATABASE_URL="sqlite:///noorify.db"
# ADMIN_ID=123456789
# TIMEZONE="Asia/Riyadh"
# INTERVAL_MIN=60
```

**كيفية الحصول على التوكن:**
1. افتح [@BotFather](https://t.me/BotFather) على تيليغرام
2. اكتب `/newbot` واتبع الخطوات
3. انسخ التوكن والصقه في الملف

---

## هيكل المشروع

```
Noorify_Bot/
├── bot.py                # نقطة البداية
├── requirements.txt      # المتطلبات
├── .env.example          # قالب الإعدادات
├── Procfile              # إعدادات Railway
├── README.md
├── LICENSE
└── handlers/             # معالجات الأوامر
```

---

## الروابط

| | الرابط |
|-|--------|
| 🤖 البوت | [t.me/Noorify_bot](https://t.me/Noorify_bot) |
| 📢 القناة | [t.me/RamiAILab](https://t.me/RamiAILab) |
| 💻 GitHub | [RamiAIlab/Noorify_Bot](https://github.com/RamiAIlab/Noorify_Bot) |
| 🌐 روابط المطور | [linktr.ee/ramibitar.dev](https://linktr.ee/ramibitar.dev) |

---

## المطور

**رامي بيطار**
[![GitHub](https://img.shields.io/badge/GitHub-RamiAIlab-181717?style=flat-square&logo=github)](https://github.com/RamiAIlab)
[![Telegram](https://img.shields.io/badge/Telegram-vx__rq-0088cc?style=flat-square&logo=telegram)](https://t.me/vx_rq)

---

## الدعم

- 🐛 **مشكلة؟** [أنشئ Issue جديدة](https://github.com/RamiAIlab/Noorify_Bot/issues/new)
- 💬 **تواصل:** [@vx_rq](https://t.me/vx_rq)

---

## الترخيص

مرخص تحت [رخصة MIT](LICENSE) — حر الاستخدام لأغراض شخصية وتجارية.

</div>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:006494,50:003554,100:051923&height=140&section=footer&text=صُنع%20بنية%20وإخلاص&fontSize=18&fontColor=61B3D4&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <sub>NoorifyBot © 2026 &nbsp;·&nbsp; مفتوح المصدر &nbsp;·&nbsp; في خدمة الذكر والتذكير</sub>
</p>

<p align="center">
  <sub>⭐ إذا أعجبك المشروع، أضف نجمة تشجيعاً ⭐</sub>
</p>
