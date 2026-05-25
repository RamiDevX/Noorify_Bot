<p align="center">
  <img src="https://images.unsplash.com/photo-2026-05-14_03-49-28.jpg" width="100%" alt="Noorify Bot Banner" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/rambos2003-lab/Noorify_Bot/main/assets/logo.jpg" width="130px" style="border-radius: 50%; box-shadow: 0px 0px 25px #00E5FF; border: 3px solid #00E5FF;" alt="Noorify Logo" /><br><br>
  <b>🌟 صَدَقَةٌ جَارِيَةٌ رَقْمِيَّةٌ 🌟</b><br>
  <sub>مِنَ التَّشَتُّتِ إِلَى الذِّكْرِ • وَمِنَ الضَّيَاعِ إِلَى الأَثَرِ</sub>
</p>

---
<img width="1456" height="720" alt="Gemini_Generated_Image_cwe4uhcwe4uhcwe4" src="https://github.com/user-attachments/assets/a70a2b7b-db39-411a-9aad-2bc0c878c888" />

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:0f2027,100:203a43&height=300&section=header&text=NOORIFY&fontSize=65&fontColor=ffffff&animation=fadeIn&fontAlignY=38" alt="Noorify Banner" />
</p>

<p align="center">
  <b>🌟 صَدَقَةٌ جَارِيَةٌ رَقْمِيَّةٌ 🌟</b><br>
  <sub>مِنَ التَّشَتُّتِ إِلَى الذِّكْرِ • وَمِنَ الضَّيَاعِ إِلَى الأَثَرِ</sub>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Aiogram-3.x-00E5FF?style=for-the-badge&logo=telegram&logoColor=black" alt="Aiogram Version"/>
  <img src="https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge" alt="Project Status"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
</p>

--- 

## 💡 فكرة المشروع

**نُورِفَاي (Noorify)** هو بوت تيليجرام تفاعلي متطور يهدف إلى دمج الأذكار والعبادات اليومية في حياة المستخدم الرقمية بأسلوب سلس ومحفز، معتمداً على هندسة برمجية غير متزامنة بالكامل لضمان السرعة والكفاءة العالية.

* **📿 مسبحة إلكترونية متطورة:** نظام تسبيح رقمي ذكي مزود بشريط تقدم تفاعلي ورتب روحية متغيرة.
* **✨ نظام بث تلقائي:** ميزة الجدولة الدورية للأذكار في المجموعات لمشرفي القنوات والمجموعات مع حماية من الحظر.
* **📊 إحصائيات دقيقة:** تحليل ذكي لمعدل الذكر اليومي لتشجيع العادات الحميدة وتقليل الإدمان الرقمي.
* **🌐 جاهز للنشر الفوري:** مهيأ بالكامل للتشغيل عبر الـ Webhook وخوادم Render أو Railway.

---

## 🧠 المعمارية والنظام الداخلي

يتكامل البوت من خلال دورة حياة غير متزامنة تتعامل مع التحديثات الواردة من واجهة برمجية تيليجرام بكفاءة:

```mermaid
flowchart TD
    A[المستخدم / الشات] -->|إرسال أمر أو نقرة زر| B[خوادم تليجرام]
    B -->|Webhook POST Request| C[خادم aiohttp المصغر]
    C -->|تغذية التحديثات بأمان| D[Aiogram Dispatcher]
    D -->|معالجة الأحداث| E[Async Engine]
    E -->|تحديث العداد| F[قاعدة بيانات الذاكرة]
    E -->|طلب تذكير دوري| G[MBI Scheduler Task]
    G -->|نشر نفحات عشوائية| A

```

--- 
## 🧩 حزمة التقنيات والبنية البرمجية (Tech Stack)

تم اختيار وهندسة حزمة التقنيات الخاصة ببوت **نُورِفَاي** بعناية فائقة لضمان أقصى درجات الكفاءة، الاستجابة السريعة، الحفاظ على موارد الخادم، ومعالجة الطلبات المتزامنة دون أي تأخير (Zero-Lag):

### 🛠️ لغة البرمجة وبيئة التطوير الأساسية (Core Engine)
<table width="100%">
  <tr>
    <td align="center" width="25%">
      <img src="https://skillicons.dev/icons?i=python" height="40px" alt="Python" /><br>
      <b>Python 3.13+</b><br>
      <sub>البيئة الأساسية وميزات إدارة الذاكرة الحديثة</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://skillicons.dev/icons?i=git" height="40px" alt="Git" /><br>
      <b>Git</b><br>
      <sub>إدارة النسخ والتحكم بالمصدر</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://skillicons.dev/icons?i=github" height="40px" alt="GitHub" /><br>
      <b>GitHub Actions</b><br>
      <sub>استضافة المستودع وإدارة الشيفرة</sub>
    </td>
    <td align="center" width="25%">
      <img src="https://skillicons.dev/icons?i=linux" height="40px" alt="Linux" /><br>
      <b>Linux OS</b><br>
      <sub>البيئة التشغيلية المستهدفة للخوادم</sub>
    </td>
  </tr>
</table>

### 📦 الإطارات والمكتبات الهندسية (Frameworks & Libraries)

<p align="left">
  <a href="https://docs.aiogram.dev/">
    <img src="https://img.shields.io/badge/Framework-Aiogram__3.x-00E5FF?style=for-the-badge&logo=telegram&logoColor=black" alt="Aiogram 3.x" />
  </a>
  <a href="https://docs.aiohttp.org/">
    <img src="https://img.shields.io/badge/Web__Server-Aiohttp__Async-🚀__00599C?style=for-the-badge&logo=python&logoColor=white" alt="Aiohttp" />
  </a>
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/Security-Python__Dotenv-🔑__💡?style=for-the-badge" alt="Dotenv" />
  </a>
  <a href="https://mermaid.js.org/">
    <img src="https://img.shields.io/badge/Architecture-Mermaid.js-🎨__FF6F61?style=for-the-badge&logo=mermaid&logoColor=white" alt="Mermaid" />
  </a>
</p>

* **`Aiogram 3.x`**: إطار عمل حديث مبني بالكامل على مفهوم البرمجة غير المتزامنة (`Asynchronous / Asyncio`) للتعامل مع واجهة برمجية تليجرام، مما يتيح معالجة آلاف الأحداث (Events) في نفس الثانية بكفاءة خطية $O(1)$.
* **`Aiohttp (Web Server)`**: خادم ويب داخلي عالي الأداء وموفر للطاقة يُستخدم لإنشاء الـ `Webhook Endpoint` لاستقبال البيانات من تليجرام فورياً ودون الحاجة لعمليات الفحص الدوري (`Polling`) المستهلكة للمعالج.
* **`Python-Dotenv`**: لتأمين مفاتيح الربط والتوكنات (`Environment Variables`) وعزل البيانات الحساسة تماماً عن شيفرة المصدر الأساسية باتباع منهجية *Twelve-Factor App*.

### 🌐 البنية التحتية وهندسة الشبكات (Infrastructure & Architecture)

<p align="center">
  <img src="https://img.shields.io/badge/Telegram_Bot_API-v7.x-0088cc?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram API"/>
  <img src="https://img.shields.io/badge/Network_Pattern-Webhook_Driven-orange?style=for-the-badge&logo=probot&logoColor=white" alt="Webhook Driven"/>
  <img src="https://img.shields.io/badge/Cloud_Hosting-Render_/_Railway-46E3B7?style=for-the-badge&logo=render&logoColor=black" alt="Render Deployment"/>
  <img src="https://img.shields.io/badge/Concurrency-Asyncio_Event_Loop-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Asyncio Loop"/>
</p>

* **نمط الشبكة (`Webhook Pattern`)**: استقبال الأحداث عبر اتصالات آمنة مشفرة (`HTTPS POST`) لضمان سرعة نقل لا تتعدى أجزاء من الملي ثانية.
* **إدارة المهام الخلفية (`Background Broadcaster Task`)**: نظام جدولة ذكي مبني كلياً داخل حلقة أحداث بايثون (`Event Loop`) يعمل في الخلفية لبث التذكيرات الدورية للمجموعات دون تعطيل تفاعل المستخدمين مع المسبحة أو القوائم.
* **الحماية من الحظر (`Flood/Rate Limit Protection`)**: تضمين فترات تأخير ميكروية مدمجة (`asyncio.sleep`) لتفادي قيود خوادم تليجرام الصارمة عند النشر الجماعي.

---

## ⚙️ دليل التثبيت والتشغيل المحلي

### 1️⃣ المتطلبات الأساسية

* بيئة عمل **Python 3.13** أو أحدث.
* رمز توكن البوت الصادر من **BotFather**.

### 2️⃣ التثبيت وإعداد المتغيرات

قم باستنساخ المستودع، وتثبيت المكتبات المطلوبة:

```bash
# استنساخ المشروع من جيت هاب
git clone [https://github.com/RamiAILab/Noorify_Bot](https://github.com/RamiAILab/Noorify_Bot)
cd Noorify_Bot

# تثبيت الحزم والمكتبات الاعتمادية
pip install -r requirements.txt

```

قم بإنشاء ملف `.env` في المجلد الرئيسي للمشروع وضع داخله الإعدادات التالية:

```env
TOKEN= ضع التكون هنا 
PORT=8080
WEBHOOK_HOST=[https://your-app-name.onrender.com](https://your-app-name.onrender.com)

```

### 3️⃣ تشغيل المشروع محلياً

```bash
python main.py

```

---

## 🔗 المنصات والروابط الرسمية (Official Links)

تفضل بزيارة منصاتنا الرسمية للتواصل، متابعة التحديثات، أو استخدام البوت مباشرة عبر الروابط المهيكلة أدناه:

<table width="100%">
  <tr>
    <td align="center" width="25%" style="background-color: #0f2027;">
      <img src="https://img.shields.io/badge/⚡_Noorify_Bot-التشغيل_الفوري-0088cc?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot" /><br><br>
      <a href="https://t.me/Noorify_bot">
        <img src="https://skillicons.dev/icons?i=telegram" height="40px" alt="Noorify Bot" />
      </a><br>
      <b><a href="https://t.me/Noorify_bot">ابدأ استخدام البوت</a></b><br>
      <sub>رابط الوصول المباشر آلياً</sub>
    </td>
    <td align="center" width="25%" style="background-color: #0f2027;">
      <img src="https://img.shields.io/badge/📢_RamiAILab-القناة_الرسمية-00E5FF?style=for-the-badge&logo=telegram&logoColor=black" alt="Tech Channel" /><br><br>
      <a href="https://t.me/RamiAILab">
        <img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram&logoColor=white" height="40px" alt="Channel" />
      </a><br>
      <b><a href="https://t.me/RamiAILab">قناتنا التقنية</a></b><br>
      <sub>متابعة آخر الحلول والابتكارات</sub>
    </td>
    <td align="center" width="25%" style="background-color: #0f2027;">
      <img src="https://img.shields.io/badge/📦_GitHub_Repo-المستودع_البرمجي-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repository" /><br><br>
      <a href="https://github.com/rambos2003-lab/Noorify_Bot">
        <img src="https://skillicons.dev/icons?i=github" height="40px" alt="GitHub" />
      </a><br>
      <b><a href="https://github.com/rambos2003-lab/Noorify_Bot">كود المشروع</a></b><br>
      <sub>مراجعة الشيفرة والمساهمة</sub>
    </td>
    <td align="center" width="25%" style="background-color: #0f2027;">
      <img src="https://img.shields.io/badge/🔗_Linktree-جميع_الروابط-orange?style=for-the-badge" alt="Linktree" /><br><br>
      <a href="https://linktr.ee/ramibitar.dev">
        <img src="https://img.shields.io/badge/Linktree-Profile-43E660?style=for-the-badge&logo=linktree&logoColor=white" height="40px" alt="Linktree" />
      </a><br>
      <b><a href="https://linktr.ee/ramibitar.dev">بوابة المطور</a></b><br>
      <sub>حساباتي وشبكاتي الاجتماعية</sub>
    </td>
  </tr>
</table>

### 👤 المطور والمسؤول التقني
* **المهندس:** رامي بيطار (Rami Bitar)
* **المستودع الشخصي للمطور على GitHub:** [RamiAIlab](https://github.com/RamiAIlab)

---

## 🎯 أهداف المشروع الإستراتيجية

* **الحد من التشتت الرقمي:** توجيه اهتمام تصفح الهاتف إلى طاعات مستمرة.
* **بناء العادات المستدامة:** ترسيخ مفهوم الأذكار اليومية من خلال الأشرطة التنافسية.
* **الأثر الاجتماعي الصالح:** تمكين المجموعات العامة من التحول إلى مجالس ذكر رقمية مباركة.

---

## 🤍 صدقة جارية

> "الدال على الخير كفاعله"
> إذا ألهمك هذا المشروع أو ساهم في بناء عاداتك الروحية، فلا تبخل علينا وعلى مبرمجي المشروع بدعوة صالحة بظهر الغيب. 🤍

---

## ⭐ دعم وتطوير المشروع

يسعدنا جداً دعمك للمشروع من خلال الضغط على زر النجمة **Star** في أعلى صفحة المستودع للمساهمة في نشره ووصوله لأكبر عدد ممكن من المطورين والمستخدمين.
