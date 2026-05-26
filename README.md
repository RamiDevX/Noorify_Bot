<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,40:0a3d62,100:0088cc&height=230&section=header&text=NOORIFY%20BOT&fontSize=78&fontColor=ffffff&fontAlignY=38&fontAlign=50&desc=نشر%20تذكيرات%20الإيمان%20اليومية%20عبر%20الأتمتة&descSize=19&descAlignY=60&descColor=a8cfe8&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <a href="https://t.me/Noorify_bot">
    <img src="https://img.shields.io/badge/بوت%20تيليغرام-نشط-0088cc?style=for-the-badge&logo=telegram&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/RamiAIlab/Noorify_Bot">
    <img src="https://img.shields.io/github/stars/RamiAIlab/Noorify_Bot?style=for-the-badge&logo=github&color=181717&logoColor=white&label=نجوم"/>
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/الرخصة-MIT-22c55e?style=for-the-badge"/>
  &nbsp;
  <img src="https://img.shields.io/badge/الحالة-نشط-00E5FF?style=for-the-badge&logo=statuspage&logoColor=white"/>
</p>

<br/>

---

## 📖 نبذة عن المشروع

<div dir="rtl">

**NoorifyBot** بوت تيليغرام مفتوح المصدر، صُمِّم لغرض واحد — أن يُدخل لحظات من التأمل الروحي وسط الروتين الرقمي اليومي.

يُرسل تذكيرات إسلامية مختارة، أدعية أصيلة، وآيات قرآنية كريمة بشكل مجدوَل وتلقائي — إلى المحادثات الخاصة، المجموعات، والقنوات دون أي تعقيد.

> في عالم مثقل بالإشعارات الفارغة، NoorifyBot هو الإشعار الذي يستحق أن تفتحه.

مبني بـ Python غير متزامن، مُجدوِل خفيف الوزن، وبصمة برمجية صغيرة — سهل الاستضافة الذاتية، قابل للتوسع، وهادف في كل رسالة يُرسلها.

</div>

<br/>

---

## ✨ المميزات

<table width="100%" dir="rtl">
  <tr>
    <td width="50%" valign="top">

**🔔 &nbsp; تذكيرات إسلامية عشوائية**
مجموعة مُختارة من الأدعية والآيات القرآنية والأحاديث — تُقدَّم بشكل عشوائي لضمان تنوع روحي حقيقي في كل رسالة.

**⏱️ &nbsp; إشعارات مجدولة**
مدعوم بـ APScheduler — اضبط وقت الإرسال وتكراره بدقة متناهية. اضبطه مرة واحدة وانسَهُ.

**🔁 &nbsp; نظام ضد التكرار**
خوارزمية ذكية تمنع تكرار المحتوى حتى يكتمل استعراض المجموعة كاملة.

  </td>
  <td width="50%" valign="top">

**💬 &nbsp; دعم متعدد المحادثات**
يعمل بسلاسة في الدردشات الخاصة، المجموعات، والقنوات — جلسة مستقلة لكل محادثة.

**🎛️ &nbsp; واجهة أزرار تفاعلية**
لوحة مفاتيح Inline نظيفة وبديهية — لا أوامر يصعب حفظها.

**▶️ &nbsp; تحكم كامل بالتشغيل**
المستخدم يتحكم بالكامل عبر `/start` و `/stop` — اشترك أو ألغِ الاشتراك في أي وقت.

  </td>
  </tr>
</table>

<br/>

---

## 🧠 التقنيات المستخدمة

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite,git,github,linux&theme=dark" height="50"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Aiogram-3.x-0088cc?style=flat-square&logo=telegram&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/APScheduler-3.x-ff6b35?style=flat-square"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Asyncio-مدمج-3776AB?style=flat-square&logo=python&logoColor=white"/>
  &nbsp;
  <img src="https://img.shields.io/badge/SQLite-قاعدة%20البيانات-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
</p>

<br/>

---

## ⚙️ التثبيت والتشغيل

```bash
# ── الخطوة 1 · استنساخ المستودع ───────────────────────────────
git clone https://github.com/RamiAIlab/Noorify_Bot.git

# ── الخطوة 2 · الدخول إلى مجلد المشروع ───────────────────────
cd Noorify_Bot

# ── الخطوة 3 · تثبيت المتطلبات ────────────────────────────────
pip install -r requirements.txt

# ── الخطوة 4 · تشغيل البوت ────────────────────────────────────
python bot.py
```

> **المتطلبات:** Python 3.11+ &nbsp;·&nbsp; تم الاختبار على Linux و Windows

<br/>

---

## 🔐 الإعدادات والمتغيرات

أنشئ ملف `.env` في جذر المشروع وأضف ما يلي:

```env
# ─────────────────────────────────────────────
#  الإعدادات الأساسية
# ─────────────────────────────────────────────
TOKEN = "YOUR_BOT_TOKEN_HERE"

# ─────────────────────────────────────────────
#  اختياري · قابلية التوسع مستقبلاً
# ─────────────────────────────────────────────
# DATABASE_URL = "sqlite:///noorify.db"
# ADMIN_ID     = 123456789
# TIMEZONE     = "Asia/Riyadh"
# INTERVAL_MIN = 60
```

> احصل على التوكن من [@BotFather](https://t.me/BotFather) على تيليغرام.

<br/>

---

## 💬 رسالة الترحيب

```
🌙  أهلاً بك في Noorify Bot

أنا هنا لأُحضر لك لحظة هادئة من الإيمان
كل يوم — تلقائياً، دون انقطاع.

اضغط ▶️ ابدأ للاشتراك في التذكيرات اليومية.

﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنفَعُ الْمُؤْمِنِينَ ﴾
                                  — سورة الذاريات، آية 55
```

<br/>

---

## 🔗 الروابط الرسمية

<table align="center" width="100%">
  <tr>
    <td align="center" width="25%">
      <a href="https://t.me/Noorify_bot">
        <img src="https://img.shields.io/badge/⚡%20Noorify%20Bot-استخدام%20مباشر-0088cc?style=for-the-badge&logo=telegram&logoColor=white"/>
      </a><br/><br/>
      <img src="https://skillicons.dev/icons?i=telegram" height="45"/>
      <br/><b>استخدم البوت</b><br/>
      <sub>🚀 تشغيل فوري</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://t.me/RamiAILab">
        <img src="https://img.shields.io/badge/📢%20القناة-تحديثات-00E5FF?style=for-the-badge&logo=telegram&logoColor=white"/>
      </a><br/><br/>
      <img src="https://skillicons.dev/icons?i=telegram" height="45"/>
      <br/><b>القناة</b><br/>
      <sub>📡 تحديثات المشروع</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/RamiAIlab/Noorify_Bot">
        <img src="https://img.shields.io/badge/📦%20GitHub-المصدر-181717?style=for-the-badge&logo=github&logoColor=white"/>
      </a><br/><br/>
      <img src="https://skillicons.dev/icons?i=github" height="45"/>
      <br/><b>المستودع</b><br/>
      <sub>💻 الكود المصدري</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://linktr.ee/ramibitar.dev">
        <img src="https://img.shields.io/badge/🔗%20Linktree-روابط%20شخصية-orange?style=for-the-badge"/>
      </a><br/><br/>
      <img src="https://skillicons.dev/icons?i=internetexplorer" height="45"/>
      <br/><b>روابطي</b><br/>
      <sub>🌐 كل الحسابات</sub>
    </td>
  </tr>
</table>

<br/>

---

## 👨‍💻 المطور

<table align="center" width="80%">
  <thead>
    <tr>
      <th align="center">الدور</th>
      <th align="center">الاسم</th>
      <th align="center">الروابط</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">🧑‍💻 &nbsp; المطور الرئيسي</td>
      <td align="center"><b>رامي بيطار</b></td>
      <td align="center">
        <a href="https://github.com/RamiAIlab">
          <img src="https://img.shields.io/badge/GitHub-RamiAIlab-181717?style=flat-square&logo=github&logoColor=white"/>
        </a>
        &nbsp;
        <a href="https://t.me/vx_rq">
          <img src="https://img.shields.io/badge/Telegram-vx__rq-0088cc?style=flat-square&logo=telegram&logoColor=white"/>
        </a>
      </td>
    </tr>
  </tbody>
</table>

<br/>

---

## 🎯 رؤية المشروع

<p align="center" dir="rtl">
  <i>
    وسط تدفق لا ينتهي من الإشعارات الرقمية الفارغة،<br/>
    يوجد NoorifyBot ليُقدِّم <b>الإشعار الوحيد الذي يستحق أن تفتحه</b> —<br/>
    كلمة تُعيد وصلك بما يهم حقاً.
  </i>
</p>

<p align="center">
  أتمتة في خدمة المعنى. تكنولوجيا كوعاء للذكر والتذكير.
</p>

<br/>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0088cc,50:0a3d62,100:0D1117&height=150&section=footer&text=صُنع%20بنية.%20يعمل%20ببساطة.&fontSize=20&fontColor=a8cfe8&fontAlignY=55&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <sub>NoorifyBot © 2025 · مفتوح المصدر · صُنع بنية وإخلاص</sub>
</p>
