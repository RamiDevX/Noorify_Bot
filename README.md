<div align="center">

<!-- ═══════════════════════════════════════ HEADER ═══════════════════════════════════════ -->

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0C1B33,25:003554,55:006494,80:0087c1,100:00B4D8&height=300&section=header&text=🌙%20NoorifyBot&fontSize=90&fontColor=ffffff&fontAlignY=40&fontAlign=50&desc=Islamic%20Daily%20Reminder%20Bot&descSize=22&descAlignY=62&descColor=ADE8F4&animation=fadeIn" alt="NoorifyBot Banner"/>

<br/>

<!-- Typing Animation -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=900&color=00B4D8&center=true&vCenter=true&width=560&lines=%F0%9F%8C%99+Daily+Islamic+Reminders;%F0%9F%93%96+Random+Quran+Verses;%F0%9F%A4%B2+Duas+%26+Adhkar;%F0%9F%93%BF+Hadiths+of+the+Day;%E2%9C%A8+Smart+Auto-Scheduling+System" alt="Typing SVG"/>

<br/><br/>

<!-- ═══ BADGES ROW 1 ═══ -->
<a href="https://t.me/Noorify_bot">
  <img src="https://img.shields.io/badge/Telegram%20Bot-@Noorify__bot-0088cc?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot"/>
</a>
&nbsp;
<a href="https://www.python.org">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</a>
&nbsp;
<a href="LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-00C896?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License"/>
</a>
&nbsp;
<img src="https://img.shields.io/badge/Status-🟢%20Active-0d1117?style=for-the-badge" alt="Active"/>

<br/><br/>

<!-- ═══ BADGES ROW 2 ═══ -->
<a href="https://github.com/RamiDevX/Noorify_Bot/stargazers">
  <img src="https://img.shields.io/github/stars/RamiDevX/Noorify_Bot?style=for-the-badge&logo=github&color=FFD700&labelColor=0d1117" alt="Stars"/>
</a>
&nbsp;
<a href="https://github.com/RamiDevX/Noorify_Bot/network/members">
  <img src="https://img.shields.io/github/forks/RamiDevX/Noorify_Bot?style=for-the-badge&logo=git&color=006494&labelColor=0d1117" alt="Forks"/>
</a>
&nbsp;
<a href="https://github.com/RamiDevX/Noorify_Bot/issues">
  <img src="https://img.shields.io/github/issues/RamiDevX/Noorify_Bot?style=for-the-badge&logo=github&color=d73a49&labelColor=0d1117" alt="Issues"/>
</a>
&nbsp;
<a href="#">
  <img src="https://img.shields.io/github/repo-size/RamiDevX/Noorify_Bot?style=for-the-badge&logo=github&color=563d7c&labelColor=0d1117" alt="Repo Size"/>
</a>

</div>

---

<div dir="rtl">

## 🌙 نبذة عن المشروع

<br/>

> ✨ *"في عالم مثقل بالإشعارات الفارغة — هذا هو الإشعار الوحيد الذي يستحق أن تفتحه."*

<br/>

**نورفاي** بوت تيليغرام ذكي يُرسل لك تذكيرات إسلامية يومياً، يحوّل هاتفك والمجموعات من فضاء التشتت إلى واحات عامرة بالذكر والأذكار التفاعلية.

🎯 **رسالتنا:** نشر الذكر والأدعية والآيات القرآنية بطريقة منظمة وتفاعلية تلائم كل مستخدم.

---

## ✨ المميزات الرئيسية

<div align="center">

| الأيقونة | الميزة | الوصف |
|:---:|:---:|:---|
| 🔔 | **تذكيرات عشوائية** | آيات وأدعية وأحاديث غير متكررة كل يوم |
| ⏱️ | **جدولة ذكية** | تعمل تلقائياً في أوقات محددة بدقة عالية |
| 💬 | **دعم شامل** | دردشات خاصة، مجموعات، وقنوات |
| 🎛️ | **واجهة سهلة** | أزرار بسيطة وواضحة للتحكم الكامل |
| ⚙️ | **تحكم كامل** | ابدأ، أوقف، أو غيّر الإعدادات في أي وقت |
| 📊 | **قاعدة بيانات** | تخزين آمن وخفيف لبيانات المستخدمين |
| 🔄 | **بدون تكرار** | خوارزمية ذكية تمنع تكرار نفس المحتوى |
| 🌐 | **دعم المجموعات** | يعمل في المجموعات والقنوات بكفاءة |

</div>

---

## ⚙️ كيف يعمل البوت؟

</div>

```mermaid
flowchart TD
    A([🙋 User sends /start]) --> B[💾 Register in Database]
    B --> C[⏰ Activate Smart Scheduler]
    C --> D{🎲 Pick Random Content}
    D -->|📖 Quran| E[Quranic Verse]
    D -->|🤲 Dua| F[Dua / Dhikr]
    D -->|📿 Hadith| G[Prophetic Hadith]
    E & F & G --> H([📨 Send to User / Group])
    H --> I{🔁 Still Active?}
    I -->|✅ Yes| C
    I -->|/stop ❌| J([🔴 Reminders Paused])
    J -->|/resume ▶️| C

    style A fill:#006494,stroke:#00B4D8,color:#fff,rx:20
    style H fill:#006494,stroke:#00B4D8,color:#fff,rx:20
    style J fill:#6B0000,stroke:#d73a49,color:#fff,rx:20
    style D fill:#003554,stroke:#006494,color:#fff
    style I fill:#003554,stroke:#006494,color:#fff
```

<div dir="rtl">

---

## 🛠️ التقنيات المستخدمة

<div align="center">

[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
&nbsp;
[![APScheduler](https://img.shields.io/badge/APScheduler-3.x-FF6B6B?style=for-the-badge&logo=clockify&logoColor=white)](https://apscheduler.readthedocs.io/)
&nbsp;
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Built--in-FFD700?style=for-the-badge&logo=python&logoColor=black)](https://docs.python.org/3/library/asyncio.html)
&nbsp;
[![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

<br/>

| 🔧 التقنية | 📋 الوصف | 📌 الإصدار |
|:---:|:---|:---:|
| 🤖 **Aiogram** | إطار عمل بوتات التيليغرام الأسرع والأقوى | `3.x` |
| ⏰ **APScheduler** | جدولة المهام والتذكيرات بدقة متناهية | `3.x` |
| ⚡ **AsyncIO** | معالجة غير متزامنة عالية الأداء | `Built-in` |
| 🗄️ **SQLite** | قاعدة بيانات خفيفة وموثوقة وسريعة | `3.x` |
| 🐍 **Python** | لغة البرمجة الأساسية للمشروع | `3.11+` |

</div>

---

## 🚀 البدء السريع

### 📋 المتطلبات الأساسية

<div align="center">

| المتطلب | الرابط | الحالة |
|:---:|:---:|:---:|
| 🐍 Python 3.11+ | [تحميل](https://python.org) | ⚠️ مطلوب |
| 📦 pip | [تحميل](https://pip.pypa.io/) | ⚠️ مطلوب |
| 🤖 Token من BotFather | [@BotFather](https://t.me/BotFather) | ⚠️ مطلوب |

</div>

<br/>

### 1️⃣ &nbsp;الاستنساخ والتثبيت

```bash
# 📥 استنساخ المشروع من GitHub
git clone https://github.com/RamiDevX/Noorify_Bot.git
cd Noorify_Bot

# 🐍 إنشاء بيئة افتراضية (موصى به بشدة)
python -m venv venv

# تفعيل البيئة — اختر حسب نظامك:
source venv/bin/activate        # 🐧 Linux / macOS
venv\Scripts\activate           # 🪟 Windows

# 📦 تثبيت جميع المكتبات المطلوبة
pip install -r requirements.txt
```

### 2️⃣ &nbsp;إعداد ملف البيئة `.env`

```env
# ⚠️  مطلوب — توكن البوت من @BotFather
TOKEN="YOUR_BOT_TOKEN_HERE"

# 🗄️  رابط قاعدة البيانات
DATABASE_URL="sqlite:///noorify.db"

# 👤  معرف حساب المشرف (اختياري)
ADMIN_ID=123456789

# 🌍  المنطقة الزمنية
TIMEZONE="Asia/Riyadh"

# ⏱️  الفاصل الزمني بين التذكيرات (بالدقائق)
INTERVAL_MIN=60
```
## 🌐 الروابط والتواصل
<div align="center">

<br/>

[![Bot](https://img.shields.io/badge/🤖%20البوت-@Noorify__bot-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Noorify_bot)
&nbsp;
[![Telegram](https://img.shields.io/badge/💬%20تيليغرام-@ramibitar-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/@ramidevx)
&nbsp;
[![GitHub](https://img.shields.io/badge/🐙%20GitHub-RamiDevX-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiDevX)

<br/>

[![Linktree](https://img.shields.io/badge/🔗%20Linktree-ramibitar-43e55e?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/ramibitarr)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/💼%20LinkedIn-Rami%20Bitar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]([https://linkedin.com/in/ramibitar](https://www.linkedin.com/public-profile/settings/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact_info%3BGuUktEu9Sj%2Bh9anoiYepLQ%3D%3D))

<br/><br/>

[![Report Bug](https://img.shields.io/badge/🐛%20إبلاغ%20عن%20مشكلة-GitHub%20Issues-d73a49?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiDevX/Noorify_Bot/issues)
&nbsp;
[![Contact](https://img.shields.io/badge/💬%20تواصل%20مباشر-Telegram-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/@ramidevx)

</div>

---

## 🤝 المساهمة والتطوير

نرحب بجميع المساهمين! إليك الخطوات:

```bash
# 1️⃣  Fork المشروع ثم استنسخه محلياً
git clone https://github.com/YOUR_USERNAME/Noorify_Bot.git

# 2️⃣  أنشئ Branch للميزة الجديدة
git checkout -b feature/AmazingFeature

# 3️⃣  طوّر واختبر ثم احفظ التغييرات
git commit -m "✨ feat: Add AmazingFeature"

# 4️⃣  ادفع إلى GitHub
git push origin feature/AmazingFeature

# 5️⃣  افتح Pull Request 🎉
```

---

## 👨‍💻 المطور

<div align="center">

<br/>

<img src="https://github.com/RamiDevX.png" width="130" style="border-radius:50%; border: 3px solid #00B4D8;" alt="RamiDevX"/>

### Rami Bitar — *RamiDevX*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-RamiDevX-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RamiDevX)
&nbsp;
[![Telegram](https://img.shields.io/badge/Telegram-@ramibitar-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ramibitar)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rami%20Bitar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ramibitar)

<br/>

<img src="https://github-readme-stats.vercel.app/api?username=RamiDevX&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00B4D8&icon_color=FFD700&text_color=ADE8F4&border_radius=12" alt="GitHub Stats" height="160"/>
&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=RamiDevX&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00B4D8&text_color=ADE8F4&layout=compact&border_radius=12" alt="Top Languages" height="160"/>

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=RamiDevX&theme=tokyonight&hide_border=true&background=0d1117&stroke=00B4D8&ring=FFD700&fire=FF6B6B&currStreakLabel=00B4D8&sideLabels=ADE8F4&dates=ADE8F4" alt="GitHub Streak" height="155"/>

</div>

---

## 📜 الترخيص

<div align="center">

<br/>

[![MIT License](https://img.shields.io/badge/📄%20License-MIT-00C896?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<br/>

هذا المشروع مرخص تحت **MIT License** — يمكنك استخدامه وتعديله وتوزيعه بحرية! ✨

</div>

---

## 🎓 مصادر مفيدة

<div align="center">

<br/>

[![Aiogram](https://img.shields.io/badge/📚%20Aiogram-Docs-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
&nbsp;
[![APScheduler](https://img.shields.io/badge/⏰%20APScheduler-Docs-FF6B6B?style=for-the-badge)](https://apscheduler.readthedocs.io/)
&nbsp;
[![Telegram API](https://img.shields.io/badge/🤖%20Telegram-Bot%20API-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)

<br/>

[![AsyncIO](https://img.shields.io/badge/⚡%20Python-AsyncIO-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/asyncio.html)
&nbsp;
[![SQLite](https://img.shields.io/badge/🗄️%20SQLite-Docs-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/docs.html)

</div>

</div>

---

<!-- ═══════════════════════════════════════ FOOTER ═══════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00B4D8,25:0087c1,55:006494,80:003554,100:0C1B33&height=170&section=footer&animation=fadeIn" alt="Footer"/>

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=RamiDevX&color=006494&style=for-the-badge&label=Profile+Views)

<br/>

**صُنع بنيّة وإخلاص ❤️‍🔥**

🌙 **NoorifyBot** © 2026 · مفتوح المصدر · في خدمة الذكر والتذكير

*⭐ إذا أعجبك المشروع، أضف نجمة لتشجيع التطوير ⭐*

</div>
