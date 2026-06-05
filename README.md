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

**NoorifyBot** بوت تيليغرام ذكي يُرسل تذكيرات إسلامية مختارة بعناية: أدعية، آيات قرآنية، وأحاديث شريفة — مجدولةً تلقائياً إلى محادثاتك الخاصة، المجموعات، والقنوات.

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

> ✓ مختبر على Linux، Windows، وmacOS

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

## الروابط والتواصل

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://t.me/Noorify_bot">
        <img src="https://img.shields.io/badge/%20%20%20%20%20%20%20%20البوت%20%20%20%20%20%20%20%20-@Noorify__bot-0088cc?style=for-the-badge&logo=telegram&logoColor=white" alt="Bot"/>
      </a>
    </td>
    <td align="center">
      <a href="https://t.me/ramibitar">
        <img src="https://img.shields.io/badge/%20%20%20%20%20%20%20تلغرام%20%20%20%20%20%20%20-0077b5?style=for-the-badge&logo=telegram&logoColor=white" alt="Channel"/>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/RamiAIlab/Noorify_Bot">
        <img src="https://img.shields.io/badge/%20%20%20%20%20GitHub%20%20%20%20%20-RamiAIlab%2FNoorify__Bot-161b22?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
      </a>
    </td>
    <td align="center">
      <a href="https://linktr.ee/ramibitar">
        <img src="https://img.shields.io/badge/%20%20%20%20روابطي%20%20%20%20-ramibitar.dev-006494?style=for-the-badge&logo=linktree&logoColor=white" alt="Linktree"/>
      </a>
    </td>
  </tr>
</table>

</div>

---

## المطور

<div align="center">

<img src="https://github.com/RamiAIlab.png" width="80" style="border-radius:50%"/>

**رامي بيطار**

[![GitHub](https://img.shields.io/badge/GitHub-RamiAIlab-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiAIlab)&nbsp;
[![Telegram](https://img.shields.io/badge/Telegram-@vx__rq-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/vx_rq)

</div>

---

## الدعم

<div align="center">

[![Issues](https://img.shields.io/badge/🐛%20%20إبلاغ%20عن%20مشكلة-GitHub%20Issues-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiAIlab/Noorify_Bot/issues/new)&nbsp;
[![Contact](https://img.shields.io/badge/💬%20%20تواصل%20مباشر-@vx__rq-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ramıibitar)

</div>

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
