import asyncio
import logging
import random
import sys
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, Any

from aiogram import Bot, Dispatcher,
from aiogram.filters import Command
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardButton, 
    InlineKeyboardMarkup, BotCommand
)
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ==============================================================================
# CONFIGURATION
# ==============================================================================
TOKEN = "YOUR_BOT_TOKEN_HERE"  # REPLACE THIS
ADMIN_ID = 1408037752
BOT_NAME = "NOORIFY AI 🌙"

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ==============================================================================
# DATA ENGINE (Enterprise Content)
# ==============================================================================
# Note: For production, these would be in a DB, here they are optimized for performance
DHIKR_DATA = {
    "dua": [
        "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
        "اللهم إني أسألك الهدى والتقى والعفاف والغنى",
        "يا مقلب القلوب ثبت قلبي على دينك",
        "اللهم اجعل القرآن ربيع قلبي ونور صدري",
        "اللهم إني أعوذ بك من الهم والحزن",
        "ربنا لا تزغ قلوبنا بعد إذ هديتنا",
        "اللهم ارزقني حسن الخاتمة",
        "اللهم اغفر لي ولوالدي وللمؤمنين والمؤمنات",
        "اللهم إني أسألك علماً نافعاً",
        "اللهم يا مصرف القلوب صرف قلوبنا على طاعتك",
        "ربنا هب لنا من أزواجنا وذرياتنا قرة أعين",
        "اللهم إني أعوذ بك من زوال نعمتك",
        "اللهم ارزقني رزقاً حلالاً طيباً",
        "اللهم ثبت قلبي على دينك",
        "اللهم اجعل لي من كل ضيق مخرجاً",
        "اللهم إني أسألك الجنة وما قرب إليها من قول أو عمل",
        "ربنا تقبل منا إنك أنت السميع العليم",
        "اللهم اغفر لي ذنبي كله دقه وجله",
        "اللهم إني أسألك العفو والعافية",
        "ربنا آتنا من لدنك رحمة وهيئ لنا من أمرنا رشداً",
        "اللهم أعني على ذكرك وشكرك وحسن عبادتك",
        "رب اشرح لي صدري ويسر لي أمري",
        "اللهم إني أسألك خير المسألة وخير الدعاء",
        "يا حي يا قيوم برحمتك أستغيث",
        "اللهم إني توكلت عليك فأعني",
        "رب اجعلني مقيم الصلاة ومن ذريتي",
        "اللهم إني أعوذ بك من شر ما صنعت",
        "اللهم ارزقني حبك وحب من يحبك",
        "يا ودود يا ودود يا ذا العرش المجيد",
        "اللهم اجعل لي نوراً في قلبي"
    ],
    "istighfar": [
        "أستغفر الله العظيم وأتوب إليه",
        "استغفر الله الذي لا إله إلا هو الحي القيوم وأتوب إليه",
        "ربي اغفر لي وتب علي إنك أنت التواب الرحيم",
        "اللهم أنت ربي لا إله إلا أنت خلقتني وأنا عبدك",
        "أستغفر الله عدد خلقه ورضا نفسه",
        "اللهم اغفر لي ما قدمت وما أخرت",
        "أستغفر الله العظيم من كل ذنب عظيم",
        "اللهم اجعلني من التوابين",
        "استغفر الله حياً وميتاً",
        "أستغفر الله لي وللمسلمين والمسلمات",
        "اللهم إني أستغفرك من كل ذنب يمنع الرزق",
        "ربي اغفر لي ولوالدي",
        "أستغفر الله الذي لا إله إلا هو وأتوب إليه",
        "اللهم اغفر لي خطيئتي وجهلي",
        "اللهم إني أستغفرك لكل ذنب أذنبته",
        "أستغفر الله العظيم لي وللمؤمنين",
        "ربي اغفر وارحم وأنت خير الراحمين",
        "أستغفر الله من كل ذنب يحبس الدعاء",
        "اللهم إني أستغفرك لذنوبي كلها",
        "أستغفر الله توبة نصوحاً",
        "رب اغفر لي خطيئتي يوم الدين",
        "اللهم إني أستغفرك من كل عمل سوء",
        "استغفر الله الذي لا إله إلا هو",
        "اللهم اغفر لي ذنبي",
        "ربي إني ظلمت نفسي فاغفر لي",
        "أستغفر الله وأتوب إليه",
        "اللهم إني أستغفرك لذنبي كله",
        "اللهم اغفر لي ما أسرفت",
        "رب اغفر وارحم",
        "أستغفر الله العلي العظيم"
    ],
    "tasbih": [
        "سبحان الله وبحمده",
        "سبحان الله العظيم",
        "لا إله إلا الله وحده لا شريك له",
        "سبحان الله والحمد لله",
        "لا حول ولا قوة إلا بالله",
        "سبحان الله عدد خلقه",
        "الله أكبر كبيراً والحمد لله كثيراً",
        "سبحان الله وبحمده عدد خلقه",
        "لا إله إلا أنت سبحانك إني كنت من الظالمين",
        "سبحان الله العظيم وبحمده",
        "سبحان الملك القدوس",
        "الله أكبر الله أكبر",
        "سبحان الله العلي العظيم",
        "الحمد لله حمداً كثيراً طيباً مباركاً فيه",
        "لا إله إلا الله الملك الحق المبين",
        "سبحان الله وبحمده سبحان الله العظيم",
        "الله أكبر وأجل",
        "سبحان الله والحمد لله ولا إله إلا الله والله أكبر",
        "لا إله إلا الله محمد رسول الله",
        "سبحان الله عدد ما خلق في السماء",
        "سبحان الله وبحمده عدد مداد كلماته",
        "الحمد لله ملء الميزان",
        "سبحان الله ملء السماوات والأرض",
        "الله أكبر عدد ما كان وما سيكون",
        "لا إله إلا الله عدد ما ذكره الذاكرون",
        "سبحان الله وبحمده عدد ما في الكون",
        "الحمد لله الذي لا إله إلا هو",
        "الله أكبر كبيراً والحمد لله كثيراً",
        "لا حول ولا قوة إلا بالله العلي العظيم",
        "سبحان الله العظيم وبحمده عدد خلقه"
    ],
    "quran": [
        "اقرأ باسم ربك الذي خلق",
        "ألا بذكر الله تطمئن القلوب",
        "فإن مع العسر يسراً",
        "واصبر لحكم ربك فإنك بأعيننا",
        "ولسوف يعطيك ربك فترضى",
        "قل هو الله أحد",
        "الله لا إله إلا هو الحي القيوم",
        "إن الله مع الصابرين",
        "وَقُل رَّبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
        "فَسُبْحَانَ اللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ",
        "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا",
        "وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ",
        "إِنَّ اللَّهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ",
        "وَلَذِكْرُ اللَّهِ أَكْبَرُ",
        "فَاذْكُرُونِي أَذْكُرْكُمْ",
        "وَهُوَ اللَّطِيفُ الْخَبِيرُ",
        "وَمَا تَوْفِيقِي إِلَّا بِاللَّهِ",
        "إِنَّ رَحْمَتَ اللَّهِ قَرِيبٌ مِّنَ الْمُحْسِنِينَ",
        "قُلْ هَلْ يَسْتَوِي الَّذِينَ يَعْلَمُونَ وَالَّذِينَ لَا يَعْلَمُونَ",
        "وَاصْبِرْ لِحُكْمِ رَبِّكَ",
        "وَسَارِعُوا إِلَىٰ مَغْفِرَةٍ مِّن رَّبِّكُمْ",
        "إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ",
        "رَّبِّ اغْفِرْ وَارْحَمْ وَأَنتَ خَيْرُ الرَّاحِمِينَ",
        "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ",
        "فَاذْكُرُوا اللَّهَ كَذِكْرِكُمْ آبَاءَكُمْ أَوْ أَشَدَّ ذِكْرًا",
        "إِنَّ اللَّهَ مَعَ الَّذِينَ اتَّقَوا",
        "وَاصْبِرْ فَإِنَّ اللَّهَ لَا يُضِيعُ أَجْرَ الْمُحْسِنِينَ",
        "فَلَا تَخَافُوهُمْ وَخَافُونِ",
        "قُلِ اللَّهُمَّ مَالِكَ الْمُلْكِ",
        "إِنَّ اللَّهَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ"
    ],
    "salah": [
        "اللهم صل وسلم على نبينا محمد",
        "اللهم صل على محمد وعلى آل محمد",
        "صلى الله عليه وسلم",
        "اللهم صلِ على محمد صلاة تحل بها العقد",
        "يا رب صل على النبي المصطفى",
        "اللهم صلِ على نبينا محمد في الأولين",
        "صلى الله على محمد صلى الله عليه وسلم",
        "اللهم صلِ على محمد وعلى آله وصحبه أجمعين",
        "اللهم صلِ وسلم على نبينا محمد عدد خلقك",
        "صلى الله عليك يا علم الهدى",
        "اللهم صلِ على محمد صلاة ترضيك وترضيه",
        "اللهم صلِ على نبينا محمد عدد ما ذكره الذاكرون",
        "صلى الله على نبينا محمد وعلى آله",
        "اللهم صلِ على محمد صلاة تفرج بها الهم",
        "اللهم صلِ على نبينا محمد صلاة تفتح بها أبواب الخير",
        "صلى الله على محمد صاحب الخلق العظيم",
        "اللهم صلِ على نبينا محمد في كل وقت وحين",
        "اللهم صلِ على نبينا محمد صلاة كاملة",
        "اللهم صلِ على نبينا محمد وعلى آله وسلم تسليماً",
        "اللهم صلِ على نبينا محمد صلاة لا تنتهي",
        "صلوات الله على النبي الأمي",
        "اللهم صل وسلم على نبينا الكريم",
        "صلى الله عليه وعلى آله وصحبه وسلم",
        "يا رب صل على الحبيب المصطفى",
        "اللهم صل وسلم وبارك على نبينا محمد",
        "صلى الله على محمد وعلى آله وصحبه وسلم",
        "اللهم صل على نبينا محمد عدد قطر المطر",
        "اللهم صل على نبينا محمد عدد ورق الشجر",
        "صلى الله عليك يا رسول الله",
        "اللهم صل على نبينا محمد في كل نفس"
    ]
}

# ==============================================================================
# DATABASE SIMULATION
# ==============================================================================
users_db: Dict[int, Dict[str, Any]] = {}
chat_settings: Dict[int, Dict[str, Any]] = {} # Reminder configs per chat
dhikr_tracker: Dict[int, Dict[str, list]] = defaultdict(lambda: {k: list(range(len(v))) for k, v in DHIKR_DATA.items()})

# ==============================================================================
# LOCALIZATION
# ==============================================================================
TEXTS = {
    "ar": {
        "welcome": "🌙 أهلاً بك في بوت نُورِفَاي الإسلامي ✨\n\nخدماتنا:\n📿 تسبيح إلكتروني\n✨ أذكار يومية ذكية\n📊 إحصائيات وإنجازات\n⏰ تذكيرات تلقائية للمجموعات",
        "tasbih": "📿 تسبيح", "random": "✨ ذكر عشوائي", "stats": "📊 إحصائياتي",
        "settings": "⚙️ الإعدادات", "back": "🔙 عودة", "main": "🏠 الرئيسية",
        "share": "🔗 مشاركة البوت", "add_group": "➕ إضافة للمجموعة", "add_channel": "📡 إضافة للقناة",
        "select_cat": "اختر تصنيف الذكر:", "tasbih_count": "عدد التسبيحات:", "rank": "الرتبة:",
        "broadcast_sent": "✅ تم الإرسال بنجاح لـ {} مستخدم.", "enter_msg": "أرسل الرسالة الآن:",
        "joined": "تاريخ الانضمام:", "profile": "👤 الملف الشخصي:",
        "reminder_set": "✅ تم ضبط التذكير كل {} ساعة.", "reminder_off": "❌ تم إيقاف التذكير.",
        "streak": "🔥 أيام النشاط:", "rank_names": ["مبتدئ 🐣", "ذاكر 🤲", "مستمر 🌟", "متميز 💎", "ولي من الذاكرين 👑"]
    },
    "tr": {
        "welcome": "🌙 Noorify İslami Bota Hoş Geldiniz ✨\n\nHizmetlerimiz:\n📿 Dijital Tesbih\n✨ Akıllı Günlük Zikirler\n📊 İstatistikler ve Başarılar\n⏰ Gruplar için Otomatik Hatırlatıcılar",
        "tasbih": "📿 Tesbih", "random": "✨ Rastgele Zikir", "stats": "📊 İstatistiklerim",
        "settings": "⚙️ Ayarlar", "back": "🔙 Geri", "main": "🏠 Ana Menü",
        "share": "🔗 Botu Paylaş", "add_group": "➕ Gruba Ekle", "add_channel": "📡 Kanala Ekle",
        "select_cat": "Kategori seçin:", "tasbih_count": "Tesbih sayısı:", "rank": "Seviye:",
        "broadcast_sent": "✅ {} kullanıcıya başarıyla gönderildi.", "enter_msg": "Mesajı gönderin:",
        "joined": "Katılım Tarihi:", "profile": "👤 Profil:",
        "reminder_set": "✅ Her {} saatte bir hatırlatıcı ayarlandı.", "reminder_off": "❌ Hatırlatıcı kapatıldı.",
        "streak": "🔥 Aktivite günü:", "rank_names": ["Başlangıç 🐣", "Zikir Yapan 🤲", "İstikrarlı 🌟", "Seçkin 💎", "Zikredenlerin Velisi 👑"]
    }
}

# ==============================================================================
# HELPERS
# ==============================================================================
def get_t(uid, key):
    lang = users_db.get(uid, {}).get("lang", "ar")
    return TEXTS.get(lang, TEXTS["ar"]).get(key, key)

def get_rank_name(count, uid):
    lang = users_db.get(uid, {}).get("lang", "ar")
    if count < 100: idx = 0
    elif count < 500: idx = 1
    elif count < 1500: idx = 2
    elif count < 5000: idx = 3
    else: idx = 4
    return TEXTS[lang]["rank_names"][idx]

def get_progress_bar(count):
    limit = 33
    filled = min(count % limit, limit)
    perc = int((filled / limit) * 10)
    return "◈" * perc + "◇" * (10 - perc)

def get_kb(uid, type="main"):
    lang = users_db.get(uid, {}).get("lang", "ar")
    kb = []
    if type == "main":
        kb = [
            [InlineKeyboardButton(text=get_t(uid, "tasbih"), callback_data="cat_tasbih"), InlineKeyboardButton(text=get_t(uid, "random"), callback_data="cat_random")],
            [InlineKeyboardButton(text=get_t(uid, "stats"), callback_data="stats"), InlineKeyboardButton(text=get_t(uid, "settings"), callback_data="settings")],
            [InlineKeyboardButton(text=get_t(uid, "share"), url="https://t.me/share/url?url=t.me/BotUsername"), InlineKeyboardButton(text=get_t(uid, "add_group"), url="https://t.me/BotUsername?startgroup=true")],
            [InlineKeyboardButton(text="🇸🇦 العربية", callback_data="lang_ar"), InlineKeyboardButton(text="🇹🇷 Türkçe", callback_data="lang_tr")]
        ]
    elif type == "categories":
        kb = [
            [InlineKeyboardButton(text="🤲 Dua", callback_data="dhikr_dua"), InlineKeyboardButton(text="💧 Istighfar", callback_data="dhikr_istighfar")],
            [InlineKeyboardButton(text="📿 Tasbih", callback_data="dhikr_tasbih"), InlineKeyboardButton(text="📖 Quran", callback_data="dhikr_quran")],
            [InlineKeyboardButton(text="❤️ Salah", callback_data="dhikr_salah")],
            [InlineKeyboardButton(text=get_t(uid, "back"), callback_data="main")]
        ]
    elif type == "settings":
        kb = [
            [InlineKeyboardButton(text="30m", callback_data="set_0.5"), InlineKeyboardButton(text="1h", callback_data="set_1")],
            [InlineKeyboardButton(text="3h", callback_data="set_3"), InlineKeyboardButton(text="6h", callback_data="set_6")],
            [InlineKeyboardButton(text="OFF", callback_data="set_0")],
            [InlineKeyboardButton(text=get_t(uid, "back"), callback_data="main")]
        ]
    elif type == "back":
        kb = [[InlineKeyboardButton(text=get_t(uid, "main"), callback_data="main")]]
    
    return InlineKeyboardMarkup(inline_keyboard=kb)

# ==============================================================================
# REMINDER ENGINE
# ==============================================================================
async def reminder_loop(bot: Bot):
    while True:
        await asyncio.sleep(60) # Check every minute
        now = datetime.now()
        for chat_id, config in chat_settings.items():
            if config['interval'] > 0:
                last_sent = config.get('last_sent', datetime.min)
                if now - last_sent >= timedelta(hours=config['interval']):
                    cat = random.choice(list(DHIKR_DATA.keys()))
                    text = random.choice(DHIKR_DATA[cat])
                    try:
                        await bot.send_message(chat_id, f"🕌 <b>التذكير الدوري:</b>\n\n{text}", parse_mode=ParseMode.HTML)
                        chat_settings[chat_id]['last_sent'] = now
                    except:
                        pass

# ==============================================================================
# BOT HANDLERS
# ==============================================================================
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    uid = message.from_user.id
    if uid not in users_db:
        users_db[uid] = {
            "name": message.from_user.full_name,
            "tasbih": 0,
            "joined": datetime.now().strftime("%Y-%m-%d"),
            "lang": "ar",
            "last_activity": datetime.now()
        }
    await message.answer(get_t(uid, "welcome"), reply_markup=get_kb(uid))

@dp.callback_query(F.data.startswith("lang_"))
async def set_lang(call: CallbackQuery):
    users_db[call.from_user.id]["lang"] = call.data.split("_")[1]
    await call.answer("Done")
    await call.message.edit_text(get_t(call.from_user.id, "welcome"), reply_markup=get_kb(call.from_user.id))

@dp.callback_query(F.data == "main")
async def main_menu(call: CallbackQuery):
    await call.message.edit_text(get_t(call.from_user.id, "welcome"), reply_markup=get_kb(call.from_user.id))

@dp.callback_query(F.data == "cat_random")
async def show_categories(call: CallbackQuery):
    await call.message.edit_text(get_t(call.from_user.id, "select_cat"), reply_markup=get_kb(call.from_user.id, "categories"))

@dp.callback_query(F.data.startswith("dhikr_"))
async def show_dhikr(call: CallbackQuery):
    cat = call.data.split("_")[1]
    uid = call.from_user.id
    tracker = dhikr_tracker[uid]
    
    if not tracker[cat]:
        tracker[cat] = list(range(len(DHIKR_DATA[cat])))
        random.shuffle(tracker[cat])
        
    idx = tracker[cat].pop()
    text = f"✨ {DHIKR_DATA[cat][idx]}"
    await call.message.edit_text(text, reply_markup=get_kb(uid, "back"))

@dp.callback_query(F.data == "cat_tasbih")
async def tasbih_view(call: CallbackQuery):
    uid = call.from_user.id
    users_db[uid]["tasbih"] += 1
    count = users_db[uid]["tasbih"]
    text = f"📿 {get_t(uid, 'tasbih_count')} {count}\n{get_progress_bar(count)}\n\n🏅 {get_t(uid, 'rank')} {get_rank_name(count, uid)}"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✨ Tap", callback_data="cat_tasbih")],
        [InlineKeyboardButton(text=get_t(uid, "back"), callback_data="main")]
    ])
    await call.message.edit_text(text, reply_markup=kb)

@dp.callback_query(F.data == "stats")
async def show_stats(call: CallbackQuery):
    uid = call.from_user.id
    u = users_db[uid]
    streak = (datetime.now() - datetime.strptime(u['joined'], "%Y-%m-%d")).days
    text = (f"{get_t(uid, 'profile')} {u['name']}\n"
            f"📿 {get_t(uid, 'tasbih_count')} {u['tasbih']}\n"
            f"🏅 {get_t(uid, 'rank')} {get_rank_name(u['tasbih'], uid)}\n"
            f"🔥 {get_t(uid, 'streak')} {streak}\n"
            f"📅 {get_t(uid, 'joined')} {u['joined']}")
    await call.message.edit_text(text, reply_markup=get_kb(uid, "back"))

@dp.callback_query(F.data == "settings")
async def show_settings(call: CallbackQuery):
    await call.message.edit_text("⚙️ Reminder Settings:", reply_markup=get_kb(call.from_user.id, "settings"))

@dp.callback_query(F.data.startswith("set_"))
async def set_reminder(call: CallbackQuery):
    interval = float(call.data.split("_")[1])
    chat_settings[call.message.chat.id] = {'interval': interval, 'last_sent': datetime.now()}
    await call.answer(get_t(call.from_user.id, "reminder_set").format(interval) if interval > 0 else get_t(call.from_user.id, "reminder_off"))

@dp.message(Command("broadcast"))
async def broadcast(message: Message):
    if message.from_user.id != ADMIN_ID: return
    text = message.text.replace("/broadcast", "").strip()
    if not text:
        await message.reply(get_t(message.from_user.id, "enter_msg"))
        return
    count = 0
    for uid in users_db:
        try:
            await message.bot.send_message(uid, text)
            count += 1
            await asyncio.sleep(0.05)
        except: continue
    await message.reply(get_t(message.from_user.id, "broadcast_sent").format(count))

# ==============================================================================
# MAIN
# ==============================================================================
async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands([
        BotCommand(command="start", description="Start Bot"),
        BotCommand(command="broadcast", description="Admin Only")
    ])
    
    # Run the reminder engine in the background
    asyncio.create_task(reminder_loop(bot))
    
    logger.info("Bot started successfully...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped.")
