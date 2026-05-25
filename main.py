import asyncio
import random
import logging
import sys
import time
import os
import urllib.parse
from datetime import datetime
from typing import Dict, Any, Callable, Awaitable
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

from aiogram import Bot, Dispatcher, F, html, BaseMiddleware
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, Message, 
    CallbackQuery, Update
)
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiohttp import web

# --- [ الإعدادات العليا ] ---
TOKEN = os.getenv("TOKEN")
MY_USER_ID = 1408037752
DEVELOPER_URL = "https://t.me/vx_rq"
TECH_CHANNEL = "https://t.me/RamiAILab"

PORT = int(os.getenv("PORT", 8080))
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://noorify-bot.onrender.com")
WEBHOOK_URL = f"{WEBHOOK_HOST}/webhook"

# --- [ Middleware: حماية السيرفر من الضغط العشوائي (Rate Limiting) ] ---
class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float = 0.5):
        self.limit = limit
        self.caches: Dict[int, float] = {}

    async def __call__(
        self, handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update, data: Dict[str, Any]
    ) -> Any:
        user_id = None
        if event.message: user_id = event.message.from_user.id
        elif event.callback_query: user_id = event.callback_query.from_user.id

        if user_id:
            now = time.time()
            if user_id in self.caches and (now - self.caches[user_id]) < self.limit:
                if event.callback_query:
                    await event.callback_query.answer("⚠️ مهلاً! الرجاء التمهل قليلاً.", show_alert=False)
                return 
            self.caches[user_id] = now

        return await handler(event, data)

# تهيئة الـ Dispatcher وتفعيل الـ Middleware
dp = Dispatcher()
dp.update.middleware(ThrottlingMiddleware(limit=0.3))

# --- [ آلة الحالة (FSM) لمدخلات المستخدمين ] ---
class UserSettings(StatesGroup):
    waiting_for_goal = State()

# --- [ قواعد البيانات المؤقتة (In-Memory Database) ] ---
active_chats: Dict[int, Dict[str, Any]] = {}
user_db: Dict[int, Dict[str, Any]] = {}

# --- [ البيانات الشاملة (لا يوجد أي اختصار) ] ---

ADHKAR_LIST = [
    "رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ الْوَهَّابُ",
    "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
    "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ نِعْمَ الْمَوْلَىٰ وَنِعْمَ النَّصِيرُ",
    "لَا إِلَهَ إِلَّا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ",
    "رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِّن لِّسَانِي يَفْقَهُوا قَوْلِي",
    "رَبِّ زِدْنِي عِلْمًا وَأَلْحِقْنِي بِالصَّالِحِينَ",
    "رَبِّ اغْفِرْ لِي وَلِوالِدَيَّ وَلِمَن دَخَلَ بَيْتِيَ مُؤْمِنًا وَلِلْمُؤْمِنِينَ وَالْمُؤْمِنَاتِ",
    "وَتُبْ عَلَيْنَا إِنَّكَ أَنتَ التَّوَّابُ الرَّحِيمُ",
    "رَبِّ اجْعَلْنِي مُقِيمَ الصَّلَاةِ وَمِن ذُرِّيَّتِي ۚ رَبَّنَا وَتَقَبَّلْ دُعَاءِ",
    "رَبِّ نَجِّنِي مِنَ الْقَوْمِ الظَّالِمِينَ",
    "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ 🕊️",
    "اللَّهُ لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ",
    "وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ",
    "إِنَّ مَعَ الْعُسْرِ يُسْرًا ✨ إِنَّ مَعَ الْعُسْرِ يُسْرًا",
    "سَلَامٌ قَوْلًا مِن رَّبٍّ رَّحِيمٍ",
    "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ 💡",
    "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ ، سُبْحَانَ اللَّهِ الْعَظِيمِ",
    "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ الَّذِي لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ وَأَتُوبُ إِلَيْهِ",
    "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ",
    "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَى نَبِيِّنَا مُحَمَّدٍ وَعَلَى آلِهِ وَصَحْبِهِ أَجْمَعِينَ",
    "يَا حَيُّ يَا قَيُّومُ بِرَحْمَتِكَ أَسْتَغِيثُ أَصْلِحْ لِي شَأْنِي كُلَّهُ",
    "اللَّهُمَّ إِنَّكَ عَفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنِّي",
    "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ",
    "الْحَمْدُ لِلَّهِ حَمْدًا كَثِيرًا طَيِّبًا مُبَارَكًا فِيهِ كَمَا يُحِبُّ رَبُّنَا وَيَرْضَى",
    "رَبِّ إِنِّي لِمَا أَنزَلْتَ إِلَيَّ مِنْ خَيْرٍ فَقِيرٌ",
    "أَعُوذُ بِكَلِمَاتِ اللَّهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ",
    "بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ",
    "يَا مُقَلِّبَ الْقُلُوبِ ثَبِّتْ قَلْبِي عَلَى دِينِكَ",
    "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ الَّتِي أَنْعَمْتَ عَلَيَّ",
    "فَسُبْحَانَ اللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ",
    "وَمَن يَتَوَكَّل عَلَى اللَّهِ فَهُوَ حَسبُهُ ۚ إِنَّ اللَّهَ بَالِغُ أَمْرِهُ",
    "رَبَّنَا اصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ ۖ إِنَّ عَذَابَهَا كَانَ غَرَامًا",
    "سُبْحَانَ رَبِّكَ رَبِّ الْعِزَّةِ عَمَّا يَصِفُونَ ✨ وَسَلَامٌ عَلَى الْمُرْسَلِينَ",
    "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ 🌍",
    "اللَّهُمَّ اكْفِنِي بِحَلَالِكَ عَنْ حَرَامِكَ وَأَغْنِنِي بِفَضْلِكَ عَمَّنْ سِوَاكَ",
    "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ ، وَالْعَجْزِ وَالْكَسَلِ",
    "مَا شَاءَ اللَّهُ لَا قُوَّةَ إِلَّا بِاللَّهِ 💎",
    "سُبْحَانَ اللَّهِ عَدَدَ مَا خَلَقَ ، سُبْحَانَ اللَّهِ مِلْءَ مَا خَلَقَ",
    "يا ذا الجلال والإكرام ، يا حي يا قيوم برحمتك أستغيث",
    "اللهم اجعل في قلبي نوراً، وفي بصري نوراً، وفي سمعي نوراً",
    "اللهم أنت ربي لا إله إلا أنت خلقتني وأنا عبدك وأنا على عهدك ووعدك ما استطعت",
    "اللهم إني أعوذ بك من علم لا ينفع، ومن قلب لا يخشع، ومن نفس لا تشبع",
]

TASBIH_TYPES = [
    "🟢 سُبْحَانَ اللَّهِ", "⚪ الْحَمْدُ لِلَّهِ", "🟡 لَا إِلَهَ إِلَّا اللَّهُ", "🟠 اللَّهُ أَكْبَرُ",
    "🔴 أَسْتَغْفِرُ اللَّهَ", "🔵 صَلِّ عَلَى مُحَمَّدٍ", "🟣 لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
    "🟤 سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "⚪ سُبْحَانَ اللَّهِ الْعَظِيمِ", "🟢 يَا حَيُّ يَا قَيُّومُ",
]

QURAN_DATA = [
    {
        "v": "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ ❤️", 
        "t": "أي: تسكن وتستأنس باسمه جل جلاله، ولا شيء ألذ للقلب من ذكر خالقه."
    },
    {
        "v": "إِنَّ مَعَ الْعُسْرِ يُسْرًا ✨", 
        "t": "بشارة عظيمة أنه كلما وُجِد العسر والمشقة، وُجِد التيسير والفرج."
    },
    {
        "v": "وَمَن يَتَوَكَّلْ عَلَى اللَّهِ فَهُوَ حَسْبُهُ 💠", 
        "t": "أي: من يعتمد على الله في أموره يكفيه ما أهمه من أمر دينه ودنياه."
    }
]

QUIZZES = [
    {"q": "كم عدد سور القرآن الكريم؟", "opts": ["110", "114", "120", "99"], "ans": 1},
    {"q": "من هو الصحابي الملقب بسيف الله المسلول؟", "opts": ["عمر بن الخطاب", "خالد بن الوليد", "علي بن أبي طالب", "سعد بن أبي وقاص"], "ans": 1},
    {"q": "ما هي السورة التي تعدل ثلث القرآن؟", "opts": ["الفاتحة", "يس", "الإخلاص", "الكوثر"], "ans": 2},
    {"q": "في أي سنة هجرية فُرض صيام رمضان؟", "opts": ["السنة الأولى", "السنة الثانية", "السنة الثالثة", "السنة الرابعة"], "ans": 1}
]

AUDIO_QURAN = [
    {"name": "سورة الفاتحة - العفاسي", "url": "https://server8.mp3quran.net/afs/001.mp3"},
    {"name": "سورة الكهف - المعيقلي", "url": "https://server12.mp3quran.net/maher/018.mp3"},
    {"name": "سورة الملك - الدوسري", "url": "https://server11.mp3quran.net/yasser/067.mp3"},
    {"name": "سورة الرحمن - السديس", "url": "https://server11.mp3quran.net/sds/055.mp3"},
    {"name": "سورة يس - الشريم", "url": "https://server7.mp3quran.net/shur/036.mp3"}
]

# --- [ الدوال المساعدة والمنطق البرمجي (Logic) ] ---
def init_user(uid: int, name: str) -> Dict[str, Any]:
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    if uid not in user_db:
        user_db[uid] = {
            "name": name, 
            "tasbih": 0, 
            "join_date": today_str,
            "last_active": today_str, 
            "streak": 1, 
            "daily_goal": 100, 
            "today_tasbih": 0
        }
    else:
        last_active = datetime.strptime(user_db[uid]["last_active"], "%Y-%m-%d").date()
        today = datetime.now().date()
        diff = (today - last_active).days
        
        if diff == 1:
            user_db[uid]["streak"] += 1
            user_db[uid]["today_tasbih"] = 0 
        elif diff > 1:
            user_db[uid]["streak"] = 1
            user_db[uid]["today_tasbih"] = 0
            
        user_db[uid]["last_active"] = today_str
        
    return user_db[uid]

def draw_progress_bar(current: int, total: int) -> str:
    if total <= 0: return "【 ◈◈◈◈◈◈◈◈◈◈ 】"
    filled = min(10, int((current / total) * 10))
    bar = "█" * filled + "░" * (10 - filled)
    percent = min(100, int((current / total) * 100))
    return f"[{bar}] {percent}%"

def get_spiritual_rank(total: int) -> tuple:
    if total >= 2500: return "ذاكر مخلص 🕊️", "🛡️"
    if total >= 1000: return "ذاكر مستمر 🌟", "🌟"
    if total >= 100: return "ساعٍ للبر 🐚", "🐚"
    return "مجاهد مبتدئ 🕊️", "🕊️"

def text_welcome() -> str:
    return (
        "🌟 مَرْحَبًا بِكَ فِي نُورِفَاي 🌟\n"
        "🕊️ النظام الإسلامي المتكامل للأذكار، التلاوات، والمسابقات.\n\n"
        "اختر من القائمة أدناه للبدء:"
    )

def get_back_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 العودة", callback_data="btn_home")]])

# --- [ الموجهات الرئيسية (Routers & Handlers) ] ---
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    bot_info = await message.bot.get_me()
    init_user(message.from_user.id, message.from_user.full_name)
    
    share_text = urllib.parse.quote("🎯 أدعوك لتفعيل بوت (نُورِفَاي) الإسلامي المتكامل ✨")
    share_url = f"https://t.me/share/url?url=https://t.me/{bot_info.username}&text={share_text}"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📿 المسبحة والورد", callback_data="btn_tasbih_menu"), 
            InlineKeyboardButton(text="🏆 لوحة الشرف", callback_data="btn_leaderboard")
        ],
        [
            InlineKeyboardButton(text="🎧 القرآن الصوتي", callback_data="btn_audio_0"), 
            InlineKeyboardButton(text="❓ سؤال ديني", callback_data="btn_quiz")
        ],
        [
            InlineKeyboardButton(text="✨ ذكر عشوائي", callback_data="btn_random"), 
            InlineKeyboardButton(text="🕋 آية وتدبر", callback_data="btn_quran")
        ],
        [
            InlineKeyboardButton(text="📊 إحصائياتي والتتابع", callback_data="btn_stats"), 
            InlineKeyboardButton(text="⚙️ إعدادات المجموعة", callback_data="btn_settings")
        ],
        [
            InlineKeyboardButton(text="➕ أضف للمجموعة", url=f"https://t.me/{bot_info.username}?startgroup=true"), 
            InlineKeyboardButton(text="🔗 شارك الأجر", url=share_url)
        ]
    ])
    await message.answer(text=text_welcome(), reply_markup=kb, parse_mode="HTML")

# --- [ نظام الورد اليومي ] ---
@dp.callback_query(F.data == "btn_set_goal")
async def btn_set_goal(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("🎯 أرسل الآن الرقم الذي تود تعيينه كورد تسبيح يومي لك (مثال: 1000):")
    await state.set_state(UserSettings.waiting_for_goal)

@dp.message(StateFilter(UserSettings.waiting_for_goal))
async def process_goal_input(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("❌ يرجى إدخال رقم صحيح (مثال: 100). المحاولة مرة أخرى:")
    
    goal = int(message.text)
    if goal < 10 or goal > 100000:
        return await message.answer("⚠️ يرجى اختيار رقم منطقي بين 10 و 100,000.")
        
    u = init_user(message.from_user.id, message.from_user.full_name)
    u["daily_goal"] = goal
    await state.clear()
    await message.answer(f"✅ تم تعيين وردك اليومي بنجاح إلى: {html.bold(str(goal))} تسبيحة.\nاستخدم /start للعودة.", parse_mode="HTML")

# --- [ المسبحة ] ---
@dp.callback_query(F.data == "btn_tasbih_menu")
async def btn_tasbih_menu(call: CallbackQuery):
    u = init_user(call.from_user.id, call.from_user.full_name)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t, callback_data=f"go_{i}") for i, t in enumerate(TASBIH_TYPES[:2])],
        [InlineKeyboardButton(text=t, callback_data=f"go_{i+2}") for i, t in enumerate(TASBIH_TYPES[2:4])],
        [InlineKeyboardButton(text=t, callback_data=f"go_{i+4}") for i, t in enumerate(TASBIH_TYPES[4:6])],
        [InlineKeyboardButton(text="🎯 ضبط الورد اليومي", callback_data="btn_set_goal")],
        [InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")]
    ])
    txt = f"📿 الورد الحالي: {u['daily_goal']} | أُنجز اليوم: {u['today_tasbih']}\nاختر نوع التسبيح:"
    await call.message.edit_text(txt, reply_markup=kb)

@dp.callback_query(F.data.startswith(("go_", "hit_")))
async def engine_tasbih(call: CallbackQuery):
    idx = int(call.data.split("_")[1])
    u = init_user(call.from_user.id, call.from_user.full_name)
    
    if call.data.startswith("hit_"):
        u["tasbih"] += 1
        u["today_tasbih"] += 1
        
    bar = draw_progress_bar(u["today_tasbih"], u["daily_goal"])
    rank_n, rank_i = get_spiritual_rank(u["tasbih"])
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="اضغط هنا ✨", callback_data=f"hit_{idx}")],
        [
            InlineKeyboardButton(text="🔄 تغيير", callback_data="btn_tasbih_menu"), 
            InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")
        ]
    ])
    
    txt = (f"{html.bold('المسبحة')} {rank_i}\n🕊️ {html.italic(TASBIH_TYPES[idx])}\n\n"
           f"🏅 الرتبة: {rank_n}\n"
           f"🎯 هدف اليوم: {bar}\n"
           f"📿 إجمالي الحسنات: {u['tasbih']}\n"
           f"🔥 التتابع: {u['streak']} أيام")
    try:
        await call.message.edit_text(txt, reply_markup=kb, parse_mode="HTML")
    except Exception:
        pass 

# --- [ الآية والتفسير ] ---
@dp.callback_query(F.data == "btn_quran")
async def btn_quran_verse(call: CallbackQuery):
    idx = random.randint(0, len(QURAN_DATA) - 1)
    verse_data = QURAN_DATA[idx]
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 عرض التفسير", callback_data=f"tafsir_{idx}")],
        [
            InlineKeyboardButton(text="🔄 آية أخرى", callback_data="btn_quran"), 
            InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")
        ]
    ])
    await call.message.edit_text(f"🕋 {html.bold('آية وتدبر:')}\n\n{html.italic(verse_data['v'])}", reply_markup=kb, parse_mode="HTML")

@dp.callback_query(F.data.startswith("tafsir_"))
async def show_tafsir(call: CallbackQuery):
    idx = int(call.data.split("_")[1])
    verse_data = QURAN_DATA[idx]
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 آية أخرى", callback_data="btn_quran")],
        [InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")]
    ])
    txt = f"🕋 {html.bold('الآية:')}\n{verse_data['v']}\n\n📖 {html.bold('التفسير الميسر:')}\n{verse_data['t']}"
    await call.message.edit_text(txt, reply_markup=kb, parse_mode="HTML")

# --- [ القرآن الصوتي بنظام الصفحات ] ---
@dp.callback_query(F.data.startswith("btn_audio_"))
async def audio_menu_paginated(call: CallbackQuery):
    page = int(call.data.split("_")[2])
    items_per_page = 3
    total_pages = (len(AUDIO_QURAN) + items_per_page - 1) // items_per_page
    
    start_idx = page * items_per_page
    end_idx = start_idx + items_per_page
    current_items = AUDIO_QURAN[start_idx:end_idx]
    
    kb_buttons = [[InlineKeyboardButton(text=item["name"], callback_data=f"playaudio_{start_idx + i}")] for i, item in enumerate(current_items)]
    
    nav_buttons = []
    if page > 0: nav_buttons.append(InlineKeyboardButton(text="⬅️ السابق", callback_data=f"btn_audio_{page-1}"))
    if page < total_pages - 1: nav_buttons.append(InlineKeyboardButton(text="التالي ➡️", callback_data=f"btn_audio_{page+1}"))
    
    if nav_buttons: kb_buttons.append(nav_buttons)
    kb_buttons.append([InlineKeyboardButton(text="🔙 العودة للرئيسية", callback_data="btn_home")])
    
    await call.message.edit_text(
        f"🎧 {html.bold('القرآن الصوتي')} (صفحة {page+1}/{total_pages})\nاختر التلاوة:", 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=kb_buttons), 
        parse_mode="HTML"
    )

@dp.callback_query(F.data.startswith("playaudio_"))
async def play_audio(call: CallbackQuery):
    idx = int(call.data.split("_")[1])
    item = AUDIO_QURAN[idx]
    await call.answer("⏳ جاري تحميل المقطع الصوتي...", show_alert=False)
    await call.message.answer_audio(audio=item["url"], caption=f"🎧 {item['name']}\n✨ عبر بوت نُورِفَاي", reply_markup=get_back_kb())

# --- [ الإحصائيات مع التتابع ] ---
@dp.callback_query(F.data == "btn_stats")
async def btn_stats_call(call: CallbackQuery):
    u = init_user(call.from_user.id, call.from_user.full_name)
    rank_n, rank_i = get_spiritual_rank(u['tasbih'])
    txt = (f"📊 {html.bold('إحصائياتك الشاملة')} {rank_i}\n\n"
           f"👤 الاسم: {u['name']}\n"
           f"🏅 الرتبة: {rank_n}\n"
           f"🔥 التتابع اليومي: {html.bold(str(u['streak']))} أيام متتالية\n"
           f"📿 إجمالي الأذكار: {u['tasbih']}\n"
           f"🎯 هدفك اليومي: {u['daily_goal']}\n"
           f"📅 الانضمام: {u['join_date']}\n")
    await call.message.edit_text(txt, reply_markup=get_back_kb(), parse_mode="HTML")

# --- [ لوحة الشرف، المسابقات، والذكر العشوائي ] ---
@dp.callback_query(F.data == "btn_leaderboard")
async def show_leaderboard(call: CallbackQuery):
    sorted_users = sorted(user_db.items(), key=lambda x: x[1]['tasbih'], reverse=True)[:10]
    txt = f"🏆 {html.bold('لوحة الشرف لأفضل الذاكرين عالمياً:')}\n\n"
    if not sorted_users: 
        txt += "لا توجد بيانات كافية بعد. كن أنت الأول! 🥇"
    else:
        for idx, (uid, data) in enumerate(sorted_users):
            medal = ["🥇", "🥈", "🥉"][idx] if idx < 3 else "🏅"
            txt += f"{medal} {html.escape(data['name'])}: {data['tasbih']} تسبيحة\n"
            
    await call.message.edit_text(txt, reply_markup=get_back_kb(), parse_mode="HTML")

@dp.callback_query(F.data == "btn_quiz")
async def send_islamic_quiz(call: CallbackQuery):
    quiz = random.choice(QUIZZES)
    await call.message.delete()
    await call.message.answer_poll(
        question=f"❓ سؤال نُورِفَاي: {quiz['q']}", 
        options=quiz['opts'], 
        type="quiz", 
        correct_option_id=quiz['ans'], 
        is_anonymous=False,
        explanation="بادر بالبحث في المصادر الموثوقة لزيادة علمك الشرعي 📚."
    )
    await call.message.answer("للمزيد من الخيارات:", reply_markup=get_back_kb())

@dp.callback_query(F.data == "btn_random")
async def btn_random_dhikr(call: CallbackQuery):
    await call.message.edit_text(f"✨ {html.bold('الذكر اليومي:')}\n\n{html.code(random.choice(ADHKAR_LIST))}", reply_markup=get_back_kb(), parse_mode="HTML")

@dp.callback_query(F.data == "btn_home")
async def back_home(call: CallbackQuery):
    bot_info = await call.bot.get_me()
    init_user(call.from_user.id, call.from_user.full_name)
    await cmd_start(call.message if isinstance(call.message, Message) else call, FSMContext(storage=dp.storage, key=call.from_user.id))

# --- [ إعدادات المجموعات ونظام البث ] ---
@dp.callback_query(F.data == "btn_settings")
async def btn_settings_callback(call: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="تفعيل التنبيه كل ساعة ⏳", callback_data="set_1")],
        [InlineKeyboardButton(text="إيقاف ❌", callback_data="set_off")],
        [InlineKeyboardButton(text="🔙 العودة", callback_data="btn_home")]
    ])
    await call.message.edit_text(f"⚙️ {html.bold('إعدادات التذكير للمجموعات')}", reply_markup=kb, parse_mode="HTML")

@dp.callback_query(F.data.startswith("set_"))
async def handle_save_settings(call: CallbackQuery):
    val = call.data.split("_")[1]
    cid = call.message.chat.id
    if val == "off":
        active_chats.pop(cid, None)
        await call.answer("✅ تم الإيقاف", show_alert=True)
    else:
        active_chats[cid] = {"interval": float(val), "last": time.time()}
        await call.answer("✅ تم التفعيل", show_alert=True)
    await back_home(call)

async def background_broadcaster(bot: Bot):
    while True:
        now = time.time()
        for cid, config in list(active_chats.items()):
            if now - config["last"] >= (config["interval"] * 3600):
                try:
                    await bot.send_message(cid, f"💠 {html.bold('تذكير:')}\n\n{random.choice(ADHKAR_LIST)}", parse_mode="HTML")
                    active_chats[cid]["last"] = now
                except Exception:
                    active_chats.pop(cid, None)
        await asyncio.sleep(60)

# --- [ Webhook & Startup ] ---
async def handle_webhook(request: web.Request) -> web.Response:
    try:
        bot: Bot = request.app['bot']
        await dp.feed_update(bot, Update(**(await request.json())))
    except Exception as e:
        logging.error(f"Error processing update: {e}")
    return web.Response(text="OK")

async def on_startup(bot: Bot):
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.sleep(1)
    await bot.set_webhook(WEBHOOK_URL)
    print(f"✅ Webhook is SET: {WEBHOOK_URL}")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.create_task(background_broadcaster(bot))
    
    app = web.Application()
    app['bot'] = bot
    app.router.add_post("/webhook", handle_webhook)
    
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", PORT).start()
    
    await on_startup(bot)
    print(f"💎 SYSTEM RUNNING. ALL FEATURES DEPLOYED WITH FULL DATA ARRAYS.")
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
