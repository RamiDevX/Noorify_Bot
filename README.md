<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,40:0a3d62,100:0088cc&height=280&section=header&text=🌟%20NOORIFY%20BOT&fontSize=85&fontColor=00D9FF&fontAlignY=40&fontAlign=50&animation=fadeIn" width="100%"/>
</p>

<div align="center">
.
### ✨ تطبيق تذكيرات إسلامية ذكي وأنيق

**بوت تيليغرام يُحول إشعاراتك إلى تجربة روحية متميزة**

</div>

<br/>

<div align="center">

[![Telegram Bot](https://img.shields.io/badge/🤖%20بوت%20تيليغرام-نشط-00D9FF?style=for-the-badge&logo=telegram&logoColor=white&labelColor=0a3d62)](https://t.me/Noorify_bot)
[![GitHub Stars](https://img.shields.io/github/stars/RamiAIlab/Noorify_Bot?style=for-the-badge&logo=github&label=⭐%20نجوم&labelColor=0a3d62&color=00D9FF)](https://github.com/RamiAIlab/Noorify_Bot)
[![Python Version](https://img.shields.io/badge/🐍%20Python-3.11+-3776AB?style=for-the-badge&labelColor=0a3d62)](https://www.python.org)
[![License](https://img.shields.io/badge/📜%20رخصة-MIT-00D9FF?style=for-the-badge&labelColor=0a3d62)](LICENSE)
[![Status](https://img.shields.io/badge/✅%20الحالة-نشط%20وجاهز-00D9FF?style=for-the-badge&labelColor=0a3d62)](https://github.com/RamiAIlab/Noorify_Bot)

</div>

---

## 📋 نبذة عن المشروع

<div align="center" dir="rtl">

> **في عالم مثقل بالإشعارات الفارغة، NoorifyBot هو الإشعار الوحيد الذي يستحق أن تفتحه** 🌙

**NoorifyBot** بوت ذكي يرسل تذكيرات إسلامية مختارة بعناية، أدعية، وآيات قرآنية مجدولة وتلقائية إلى محادثاتك الخاصة والمجموعات والقنوات.

مبني بـ **Python غير متزامن**، مُجدوِل خفيف الوزن، وبصمة برمجية صغيرة — سهل الاستضافة الذاتية، قابل للتوسع، وهادف.

</div>

---

## ✨ المميزات الرئيسية

<table width="100%" dir="rtl">
  <tr>
    <td width="50%" valign="top">

### 🔔 تذكيرات عشوائية ذكية
مجموعة مُختارة من الأدعية والآيات القرآنية والأحاديث — تُقدَّم بشكل عشوائي لضمان تنوع روحي حقيقي في كل رسالة

### ⏱️ إشعارات مجدولة دقيقة
مدعوم بـ **APScheduler** — اضبط وقت الإرسال وتكراره بدقة متناهية. اضبطه مرة واحدة وانسَهُ

### 🔁 نظام ضد التكرار الذكي
خوارزمية متقدمة تمنع تكرار المحتوى حتى يكتمل استعراض المجموعة كاملة

    </td>
    <td width="50%" valign="top">

### 💬 دعم متعدد المحادثات
يعمل بسلاسة في الدردشات الخاصة، المجموعات، والقنوات — جلسة مستقلة لكل محادثة

### 🎛️ واجهة أزرار تفاعلية
لوحة مفاتيح **Inline** نظيفة وبديهية — لا أوامر معقدة يصعب حفظها

### ▶️ تحكم كامل بالتشغيل
أنت تتحكم بالكامل عبر `/start` و `/stop` — اشترك أو ألغِ الاشتراك في أي وقت

    </td>
  </tr>
</table>

---

## 🛠️ التقنيات المستخدمة

<div align="center">

<img src="https://skillicons.dev/icons?i=python,sqlite,git,github,linux&theme=dark" height="55" alt="Tech Stack"/>

| التقنية | الإصدار | الوصف |
|:---:|:---:|:---|
| **Aiogram** | `3.x` | إطار عمل تيليغرام غير متزامن |
| **APScheduler** | `3.x` | جدولة المهام الذكية والدقيقة |
| **Asyncio** | مدمج | معالجة غير متزامنة محسّنة |
| **SQLite** | قاعدة بيانات | تخزين البيانات الآمن والخفيف |

</div>

---

## 🚀 التثبيت والتشغيل

### المتطلبات المسبقة
- **Python 3.11+** ✅
- **pip** (مدير الحزم) ✅
- **توكن بوت تيليغرام** من [@BotFather](https://t.me/BotFather)

### خطوات التثبيت

```bash
# ┌─────────────────────────────────────────┐
# │ 1️⃣  استنساخ المستودع                  │
# └─────────────────────────────────────────┘
git clone https://github.com/RamiAIlab/Noorify_Bot.git

# ┌─────────────────────────────────────────┐
# │ 2️⃣  الدخول إلى مجلد المشروع           │
# └─────────────────────────────────────────┘
cd Noorify_Bot

# ┌─────────────────────────────────────────┐
# │ 3️⃣  تثبيت المتطلبات                   │
# └─────────────────────────────────────────┘
pip install -r requirements.txt

# ┌─────────────────────────────────────────┐
# │ 4️⃣  تشغيل البوت                       │
# └─────────────────────────────────────────┘
python bot.py
```

> ✅ تم الاختبار على **Linux** و **Windows** و **macOS**

---

## ⚙️ الإعدادات والمتغيرات

أنشئ ملف `.env` في جذر المشروع وأضف المتغيرات التالية:

```env
# ╔═══════════════════════════════════════════════════════╗
# ║        🔐 الإعدادات الأساسية والضرورية             ║
# ╚═══════════════════════════════════════════════════════╝

# توكن البوت من @BotFather
TOKEN = "YOUR_BOT_TOKEN_HERE"

# ╔═══════════════════════════════════════════════════════╗
# ║        📌 الإعدادات الاختيارية (متقدمة)           ║
# ╚═══════════════════════════════════════════════════════╝

# عنوان قاعدة البيانات
# DATABASE_URL = "sqlite:///noorify.db"

# معرّف المسؤول للأوامر الحساسة
# ADMIN_ID = 123456789

# المنطقة الزمنية (Asia/Riyadh, Europe/London, إلخ)
# TIMEZONE = "Asia/Riyadh"

# الحد الأدنى للفترة الزمنية بالدقائق
# INTERVAL_MIN = 60
```

**كيفية الحصول على التوكن؟**
- توجه إلى [@BotFather](https://t.me/BotFather) على تيليغرام
- اكتب `/start` ثم اتبع الخطوات
- اختر `/newbot` وأكمل العملية
- انسخ التوكن والصقه في ملف `.env`

---

## 📁 هيكل المشروع

```
Noorify_Bot/
├── 📄 bot.py                 # نقطة البداية الرئيسية
├── 📄 requirements.txt        # المتطلبات والمكتبات
├── 📄 .env.example           # قالب الإعدادات
├── 📄 Procfile               # إعدادات النشر على Railway
├── 📋 README.md              # هذا الملف
├── 📋 LICENSE                # رخصة MIT
└── 📁 handlers/              # معالجات الأوامر والرسائل
```

---

## 🔗 الروابط الرسمية

<table align="center" width="100%">
  <tr>
    <td align="center" width="25%">
      <a href="https://t.me/Noorify_bot">
        <img src="https://img.shields.io/badge/⚡%20استخدم%20البوت-مباشر%20الآن-00D9FF?style=for-the-badge&logo=telegram&logoColor=white&labelColor=0a3d62" width="100%"/>
      </a><br/><br/>
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/telegram/telegram-original.svg" height="50" alt="Telegram"/><br/>
      <b>🤖 البوت</b><br/>
      <sub>اضغط للاستخدام الفوري</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://t.me/RamiAILab">
        <img src="https://img.shields.io/badge/📢%20القناة-تحديثات%20مستمرة-00D9FF?style=for-the-badge&logo=telegram&logoColor=white&labelColor=0a3d62" width="100%"/>
      </a><br/><br/>
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/telegram/telegram-original.svg" height="50" alt="Telegram Channel"/><br/>
      <b>📡 القناة</b><br/>
      <sub>متابعة التحديثات والأخبار</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/RamiAIlab/Noorify_Bot">
        <img src="https://img.shields.io/badge/📦%20المستودع-الكود%20المصدري-00D9FF?style=for-the-badge&logo=github&logoColor=white&labelColor=0a3d62" width="100%"/>
      </a><br/><br/>
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" height="50" alt="GitHub"/><br/>
      <b>💻 GitHub</b><br/>
      <sub>الوصول للكود المصدري</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://linktr.ee/ramibitar.dev">
        <img src="https://img.shields.io/badge/🔗%20روابطي-شخصية-00D9FF?style=for-the-badge&labelColor=0a3d62" width="100%"/>
      </a><br/><br/>
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/chrome/chrome-original.svg" height="50" alt="Links"/><br/>
      <b>🌐 الروابط</b><br/>
      <sub>كل الحسابات والمشاريع</sub>
    </td>
  </tr>
</table>

---

## 👨‍💻 المطور والفريق

<div align="center">

| الدور | الاسم | الروابط |
|:---:|:---:|:---:|
| 🧑‍💻 **المطور الرئيسي** | **رامي بيطار** | [![GitHub](https://img.shields.io/badge/GitHub-RamiAIlab-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RamiAIlab) [![Telegram](https://img.shields.io/badge/Telegram-vx__rq-0088cc?style=flat-square&logo=telegram&logoColor=white)](https://t.me/vx_rq) |

</div>

---

## 🎯 رؤية المشروع

<p align="center" dir="rtl">
  <b>
    وسط تدفق لا ينتهي من الإشعارات الرقمية الفارغة،<br/>
    يوجد <b>NoorifyBot</b> ليُقدِّم <b style="color: #00D9FF">الإشعار الوحيد الذي يستحق أن تفتحه</b> —<br/>
    كلمة تُعيد وصلك بما يهم حقاً في حياتك.
  </b>
</p>

<p align="center">
  <i>"أتمتة في خدمة المعنى. تكنولوجيا كوعاء للذكر والتذكير."</i>
</p>

---

## 📊 الإحصائيات والمعلومات

<div align="center">

| المعلومة | القيمة |
|:---:|:---|
| 🐍 لغة البرمجة | Python 3.11+ |
| 📦 الحجم | خفيف الوزن وفعّال |
| ⚡ الأداء | غير متزامن وسريع |
| 📱 التوافق | جميع الأنظمة (Linux, Windows, macOS) |
| 🔒 الأمان | توكن آمن وبيانات محمية |
| 📜 الرخصة | MIT (مفتوح المصدر) |

</div>

---

## 📞 الدعم والمساعدة

هل واجهت مشكلة أو لديك اقتراح؟

- 📧 **تواصل عبر GitHub Issues**: [أنشئ قضية جديدة](https://github.com/RamiAIlab/Noorify_Bot/issues/new)
- 💬 **راسلني على Telegram**: [@vx_rq](https://t.me/vx_rq)
- 📢 **تابع القناة للتحديثات**: [@RamiAILab](https://t.me/RamiAILab)

---

## 📜 الترخيص

هذا المشروع مرخص تحت **رخصة MIT** — يمكنك استخدامه بحرية في مشاريعك الشخصية والتجارية.

اطّلع على ملف [LICENSE](LICENSE) للمزيد من التفاصيل.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0088cc,50:0a3d62,100:0D1117&height=180&section=footer&text=✨%20صُنع%20بنية%20وإخلاص&fontSize=24&fontColor=00D9FF&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <sub>
    <b>NoorifyBot © 2026</b><br/>
    مفتوح المصدر • صُنع بنية وإخلاص • في خدمة الذكر والتذكير<br/>
    <b style="color: #0088cc">لا إله إلا الله وحده لا شريك له</b>
  </sub>
</p>

<div align="center">

**⭐ إذا أعجبك المشروع، لا تنسَ إضافة نجمة! ⭐**

</div>
