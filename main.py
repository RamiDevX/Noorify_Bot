# ============================================================
# Noorify Islamic Telegram Bot
# Full Professional Version - Aiogram 3
# ============================================================

import asyncio
import logging
import os
import random
import sys
import time
import urllib.parse
from datetime import datetime
from typing import Dict, Any, Callable, Awaitable

from dotenv import load_dotenv
from aiohttp import web

from aiogram import Bot, Dispatcher, F, html, BaseMiddleware
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
    Update,
)

# ============================================================
# تحميل المتغيرات
# ============================================================

load_dotenv()

TOKEN = os.getenv("TOKEN")
PORT = int(os.getenv("PORT", 8080))
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://your-bot.onrender.com")
WEBHOOK_URL = f"{WEBHOOK_HOST}/webhook"

OWNER_ID = 1408037752
DEVELOPER_URL = "https://t.me/vx_rq"
TECH_CHANNEL = "https://t.me/RamiAILab"

# ============================================================
# تسجيل الأخطاء
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ============================================================
# قواعد بيانات مؤقتة
# ============================================================

user_db: Dict[int, Dict[str, Any]] = {}
active_chats: Dict[int, Dict[str, Any]] = {}

# ============================================================
# Middleware حماية من السبام
# ============================================================

class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit: float = 0.4):
        self.limit = limit
        self.cache: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ):

        user_id = None

        if event.message:
            user_id = event.message.from_user.id

        elif event.callback_query:
            user_id = event.callback_query.from_user.id

        if user_id:
            now = time.time()

            if user_id in self.cache:
                if now - self.cache[user_id] < self.limit:

                    if event.callback_query:
                        await event.callback_query.answer(
                            "⚠️ انتظر قليلاً قبل الضغط مرة أخرى",
                            show_alert=False
                        )
                    return

            self.cache[user_id] = now

        return await handler(event, data)

# ============================================================
# Dispatcher
# ============================================================

dp = Dispatcher()
dp.update.middleware(ThrottlingMiddleware())

# ============================================================
# الحالات FSM
# ============================================================

class UserSettings(StatesGroup):
    waiting_for_goal = State()

class BroadcastState(StatesGroup):
    waiting_for_message = State()

# ============================================================
# بيانات الأذكار
# ============================================================

ADHKAR_LIST = [
    "سُبْحَانَ اللَّهِ",
    "الْحَمْدُ لِلَّهِ",
    "اللَّهُ أَكْبَرُ",
    "لَا إِلَهَ إِلَّا اللَّهُ",
    "أَسْتَغْفِرُ اللَّهَ",
    "اللهم صل وسلم على نبينا محمد ﷺ",
    "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
    "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ",
    "اللَّهُمَّ اجْعَلْ الْقُرْآنَ رَبِيعَ قُلُوبِنَا",
    "اللَّهُمَّ اغْفِرْ لِي وَلِوَالِدَيَّ",
    "رَبِّ زِدْنِي عِلْمًا",
    "رَبِّ اشْرَحْ لِي صَدْرِي",
    "اللَّهُمَّ إِنَّكَ عَفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنَّا",
    "يَا حَيُّ يَا قَيُّومُ بِرَحْمَتِكَ أَسْتَغِيثُ",
    "اللَّهُمَّ ارْزُقْنَا حُسْنَ الْخَاتِمَةِ",
    "اللَّهُمَّ ثَبِّتْ قُلُوبَنَا عَلَى دِينِكَ",
    "اللَّهُمَّ اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ",
    "اللَّهُمَّ ارْحَمْنَا بِرَحْمَتِكَ",
    "اللَّهُمَّ اجْعَلْنَا مِنَ الذَّاكِرِينَ",
    "اللَّهُمَّ أَجِرْنَا مِنَ النَّارِ",
]

# ============================================================
# أنواع التسبيح
# ============================================================

TASBIH_TYPES = [
    "🟢 سبحان الله",
    "⚪ الحمد لله",
    "🟡 لا إله إلا الله",
    "🟠 الله أكبر",
    "🔴 أستغفر الله",
    "🔵 صل على محمد",
    "🟣 لا حول ولا قوة إلا بالله",
    "🟤 سبحان الله وبحمده",
    "⚫ سبحان الله العظيم",
    "🟢 يا حي يا قيوم",
]

# ============================================================
# آيات
# ============================================================

QURAN_DATA = [
    {
        "v": "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ ❤️",
        "t": "القلوب لا تطمئن إلا بذكر الله"
    },
    {
        "v": "إِنَّ مَعَ الْعُسْرِ يُسْرًا ✨",
        "t": "كل ضيق يعقبه فرج بإذن الله"
    },
    {
        "v": "وَمَن يَتَوَكَّلْ عَلَى اللَّهِ فَهُوَ حَسْبُهُ 💠",
        "t": "من توكل على الله كفاه"
    },
]

# ============================================================
# مسابقات
# ============================================================

QUIZZES = [
    {
        "q": "كم عدد سور القرآن الكريم؟",
        "opts": ["110", "114", "120", "99"],
        "ans": 1,
    },
    {
        "q": "من هو سيف الله المسلول؟",
        "opts": [
            "عمر بن الخطاب",
            "خالد بن الوليد",
            "علي بن أبي طالب",
            "أبو عبيدة",
        ],
        "ans": 1,
    },
]

# ============================================================
# قرآن صوتي
# ============================================================

AUDIO_QURAN = [
    {
        "name": "سورة الفاتحة - العفاسي",
        "url": "https://server8.mp3quran.net/afs/001.mp3",
    },
    {
        "name": "سورة الكهف - المعيقلي",
        "url": "https://server12.mp3quran.net/maher/018.mp3",
    },
    {
        "name": "سورة الملك - الدوسري",
        "url": "https://server11.mp3quran.net/yasser/067.mp3",
    },
]

# ============================================================
# دوال مساعدة
# ============================================================


def init_user(uid: int, name: str):

    today = datetime.now().strftime("%Y-%m-%d")

    if uid not in user_db:
        user_db[uid] = {
            "name": name,
            "tasbih": 0,
            "today_tasbih": 0,
            "daily_goal": 100,
            "join_date": today,
            "last_active": today,
            "streak": 1,
        }

    return user_db[uid]


# ============================================================
# شريط التقدم
# ============================================================


def draw_progress_bar(current, total):

    if total <= 0:
        return "[░░░░░░░░░░] 0%"

    percentage = min(int((current / total) * 100), 100)

    filled = percentage // 10

    bar = "█" * filled + "░" * (10 - filled)

    return f"[{bar}] {percentage}%"

# ============================================================
# الرتب
# ============================================================


def get_spiritual_rank(total):

    if total >= 10000:
        return "👑 إمام الذاكرين"

    if total >= 5000:
        return "🏆 ذاكر محترف"

    if total >= 1000:
        return "🌟 ذاكر مستمر"

    if total >= 100:
        return "✨ محب للذكر"

    return "🕊️ مبتدئ"

# ============================================================
# رسالة البداية
# ============================================================


def welcome_text(name: str):

    return f"""
🌟 أهلاً بك {html.bold(name)} في بوت نوريفاي الإسلامي المتكامل

هذا البوت يوفر لك:

📿 مسبحة إلكترونية ذكية
🕋 آيات وتدبر
🎧 قرآن صوتي
🏆 لوحة المتصدرين
🔥 نظام التتابع اليومي
🎯 أهداف يومية
❓ مسابقات إسلامية
📊 إحصائيات كاملة
📢 نظام بث احترافي

━━━━━━━━━━━━━━━
👨‍💻 المطور:
{DEVELOPER_URL}

📢 القناة التقنية:
{TECH_CHANNEL}
━━━━━━━━━━━━━━━
"""

# ============================================================
# زر رجوع
# ============================================================


def back_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 العودة",
                    callback_data="home"
                )
            ]
        ]
    )

# ============================================================
# القائمة الرئيسية
# ============================================================


def main_menu(bot_username: str):

    share_text = urllib.parse.quote(
        "✨ جرب بوت نوريفاي الإسلامي الرائع"
    )

    share_url = (
        f"https://t.me/share/url?url=https://t.me/{bot_username}&text={share_text}"
    )

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📿 المسبحة",
                    callback_data="tasbih_menu"
                ),
                InlineKeyboardButton(
                    text="✨ ذكر عشوائي",
                    callback_data="random_dhikr"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🕋 آية وتدبر",
                    callback_data="quran"
                ),
                InlineKeyboardButton(
                    text="🎧 القرآن الصوتي",
                    callback_data="audio_menu"
                )
            ],

            [
                InlineKeyboardButton(
                    text="❓ سؤال ديني",
                    callback_data="quiz"
                ),
                InlineKeyboardButton(
                    text="🏆 لوحة الشرف",
                    callback_data="leaderboard"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📊 إحصائياتي",
                    callback_data="stats"
                ),
                InlineKeyboardButton(
                    text="⚙️ الإعدادات",
                    callback_data="settings"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📢 القناة التقنية",
                    url=TECH_CHANNEL
                ),
                InlineKeyboardButton(
                    text="👨‍💻 المطور",
                    url=DEVELOPER_URL
                )
            ],

            [
                InlineKeyboardButton(
                    text="➕ أضف البوت لمجموعة",
                    url=f"https://t.me/{bot_username}?startgroup=true"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔗 مشاركة البوت",
                    url=share_url
                )
            ]
        ]
    )

# ============================================================
# أمر البداية
# ============================================================

@dp.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):

    await state.clear()

    user = init_user(
        message.from_user.id,
        message.from_user.full_name
    )

    bot_info = await message.bot.get_me()

    await message.answer(
        welcome_text(user['name']),
        reply_markup=main_menu(bot_info.username),
        parse_mode="HTML"
    )

# ============================================================
# الصفحة الرئيسية
# ============================================================

@dp.callback_query(F.data == "home")
async def back_home(call: CallbackQuery, state: FSMContext):

    await state.clear()

    bot_info = await call.bot.get_me()

    await call.message.edit_text(
        welcome_text(call.from_user.full_name),
        reply_markup=main_menu(bot_info.username),
        parse_mode="HTML"
    )

# ============================================================
# الذكر العشوائي
# ============================================================

@dp.callback_query(F.data == "random_dhikr")
async def random_dhikr(call: CallbackQuery):

    await call.message.edit_text(
        f"✨ {random.choice(ADHKAR_LIST)}",
        reply_markup=back_keyboard()
    )

# ============================================================
# الآيات
# ============================================================

@dp.callback_query(F.data == "quran")
async def quran_handler(call: CallbackQuery):

    item = random.choice(QURAN_DATA)

    text = (
        f"🕋 {html.bold('آية اليوم')}\n\n"
        f"{item['v']}\n\n"
        f"📖 {item['t']}"
    )

    await call.message.edit_text(
        text,
        reply_markup=back_keyboard(),
        parse_mode="HTML"
    )

# ============================================================
# القرآن الصوتي
# ============================================================

@dp.callback_query(F.data == "audio_menu")
async def audio_menu(call: CallbackQuery):

    buttons = []

    for index, item in enumerate(AUDIO_QURAN):
        buttons.append([
            InlineKeyboardButton(
                text=item['name'],
                callback_data=f"audio_{index}"
            )
        ])

    buttons.append([
        InlineKeyboardButton(
            text="🔙 العودة",
            callback_data="home"
        )
    ])

    await call.message.edit_text(
        "🎧 اختر التلاوة",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=buttons
        )
    )

# ============================================================
# تشغيل الصوت
# ============================================================

@dp.callback_query(F.data.startswith("audio_"))
async def play_audio(call: CallbackQuery):

    index = int(call.data.split("_")[1])

    item = AUDIO_QURAN[index]

    await call.message.answer_audio(
        audio=item['url'],
        caption=item['name'],
        reply_markup=back_keyboard()
    )

# ============================================================
# المسابقة
# ============================================================

@dp.callback_query(F.data == "quiz")
async def quiz_handler(call: CallbackQuery):

    quiz = random.choice(QUIZZES)

    await call.message.answer_poll(
        question=quiz['q'],
        options=quiz['opts'],
        type="quiz",
        correct_option_id=quiz['ans'],
        is_anonymous=False,
    )

# ============================================================
# لوحة الشرف
# ============================================================

@dp.callback_query(F.data == "leaderboard")
async def leaderboard_handler(call: CallbackQuery):

    sorted_users = sorted(
        user_db.items(),
        key=lambda x: x[1]['tasbih'],
        reverse=True
    )[:10]

    text = "🏆 لوحة الشرف\n\n"

    if not sorted_users:
        text += "لا يوجد مستخدمون بعد"

    else:

        for idx, (_, data) in enumerate(sorted_users, start=1):
            text += (
                f"{idx}. {data['name']} - "
                f"{data['tasbih']}\n"
            )

    await call.message.edit_text(
        text,
        reply_markup=back_keyboard()
    )

# ============================================================
# الإحصائيات
# ============================================================

@dp.callback_query(F.data == "stats")
async def stats_handler(call: CallbackQuery):

    user = init_user(
        call.from_user.id,
        call.from_user.full_name
    )

    progress = draw_progress_bar(
        user['today_tasbih'],
        user['daily_goal']
    )

    rank = get_spiritual_rank(user['tasbih'])

    text = f"""
📊 إحصائياتك الكاملة

👤 الاسم: {user['name']}
🏅 الرتبة: {rank}
📿 إجمالي التسبيحات: {user['tasbih']}
🎯 الهدف اليومي: {user['daily_goal']}
🔥 تتابع الأيام: {user['streak']}
📅 تاريخ الانضمام: {user['join_date']}

{progress}
"""

    await call.message.edit_text(
        text,
        reply_markup=back_keyboard()
    )

# ============================================================
# المسبحة
# ============================================================

@dp.callback_query(F.data == "tasbih_menu")
async def tasbih_menu(call: CallbackQuery):

    buttons = []

    for index, item in enumerate(TASBIH_TYPES):
        buttons.append([
            InlineKeyboardButton(
                text=item,
                callback_data=f"tasbih_{index}"
            )
        ])

    buttons.append([
        InlineKeyboardButton(
            text="🎯 تغيير الهدف",
            callback_data="set_goal"
        )
    ])

    buttons.append([
        InlineKeyboardButton(
            text="🔙 العودة",
            callback_data="home"
        )
    ])

    await call.message.edit_text(
        "📿 اختر نوع التسبيح",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=buttons
        )
    )

# ============================================================
# التسبيح
# ============================================================

@dp.callback_query(F.data.startswith("tasbih_"))
async def tasbih_counter(call: CallbackQuery):

    index = int(call.data.split("_")[1])

    user = init_user(
        call.from_user.id,
        call.from_user.full_name
    )

    user['tasbih'] += 1
    user['today_tasbih'] += 1

    progress = draw_progress_bar(
        user['today_tasbih'],
        user['daily_goal']
    )

    text = f"""
📿 {TASBIH_TYPES[index]}

📊 العدد الكلي: {user['tasbih']}
🎯 تقدم الهدف:\n{progress}
"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✨ تسبيحة",
                    callback_data=f"tasbih_{index}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔄 تغيير",
                    callback_data="tasbih_menu"
                ),
                InlineKeyboardButton(
                    text="🔙 العودة",
                    callback_data="home"
                )
            ]
        ]
    )

    await call.message.edit_text(
        text,
        reply_markup=keyboard
    )

# ============================================================
# تغيير الهدف
# ============================================================

@dp.callback_query(F.data == "set_goal")
async def set_goal(call: CallbackQuery, state: FSMContext):

    await state.set_state(UserSettings.waiting_for_goal)

    await call.message.edit_text(
        "🎯 أرسل الهدف اليومي الجديد"
    )

# ============================================================
# استقبال الهدف
# ============================================================

@dp.message(StateFilter(UserSettings.waiting_for_goal))
async def process_goal(message: Message, state: FSMContext):

    if not message.text.isdigit():
        return await message.answer(
            "❌ أرسل رقم فقط"
        )

    goal = int(message.text)

    user = init_user(
        message.from_user.id,
        message.from_user.full_name
    )

    user['daily_goal'] = goal

    await state.clear()

    await message.answer(
        f"✅ تم تعيين الهدف إلى {goal}"
    )

# ============================================================
# الإعدادات
# ============================================================

@dp.callback_query(F.data == "settings")
async def settings_handler(call: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⏰ تفعيل التذكير",
                    callback_data="enable_reminder"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ تعطيل التذكير",
                    callback_data="disable_reminder"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 العودة",
                    callback_data="home"
                )
            ]
        ]
    )

    await call.message.edit_text(
        "⚙️ إعدادات البوت",
        reply_markup=keyboard
    )

# ============================================================
# تفعيل التذكير
# ============================================================

@dp.callback_query(F.data == "enable_reminder")
async def enable_reminder(call: CallbackQuery):

    active_chats[call.message.chat.id] = {
        "enabled": True,
        "last": time.time(),
    }

    await call.answer(
        "✅ تم تفعيل التذكير"
    )

# ============================================================
# تعطيل التذكير
# ============================================================

@dp.callback_query(F.data == "disable_reminder")
async def disable_reminder(call: CallbackQuery):

    active_chats.pop(call.message.chat.id, None)

    await call.answer(
        "❌ تم تعطيل التذكير"
    )

# ============================================================
# أمر broadcast
# ============================================================

@dp.message(Command("broadcast"))
async def broadcast_command(message: Message, state: FSMContext):

    if message.from_user.id != OWNER_ID:
        return

    await state.set_state(BroadcastState.waiting_for_message)

    await message.answer(
        "📢 أرسل رسالة البث الآن"
    )

# ============================================================
# تنفيذ البث
# ============================================================

@dp.message(StateFilter(BroadcastState.waiting_for_message))
async def process_broadcast(message: Message, state: FSMContext):

    if message.from_user.id != OWNER_ID:
        return

    sent = 0
    failed = 0

    for user_id in list(user_db.keys()):

        try:
            await message.bot.send_message(
                user_id,
                f"📢 رسالة جديدة من إدارة نوريفاي\n\n{message.text}"
            )
            sent += 1

        except Exception:
            failed += 1

    await state.clear()

    await message.answer(
        f"✅ تم الإرسال إلى {sent}\n❌ فشل: {failed}"
    )

# ============================================================
# مهمة الخلفية
# ============================================================

async def background_reminder(bot: Bot):

    while True:

        for chat_id in list(active_chats.keys()):

            try:
                await bot.send_message(
                    chat_id,
                    f"✨ تذكير\n\n{random.choice(ADHKAR_LIST)}"
                )

            except Exception:
                active_chats.pop(chat_id, None)

        await asyncio.sleep(3600)

# ============================================================
# Webhook
# ============================================================

async def handle_webhook(request: web.Request):

    bot: Bot = request.app['bot']

    data = await request.json()

    update = Update(**data)

    await dp.feed_update(bot, update)

    return web.Response(text="OK")

# ============================================================
# التشغيل
# ============================================================

async def on_startup(bot: Bot):

    await bot.delete_webhook(drop_pending_updates=True)

    await bot.set_webhook(WEBHOOK_URL)

    logging.info(f"Webhook Set: {WEBHOOK_URL}")

# ============================================================
# Main
# ============================================================

async def main():

    if not TOKEN:
        raise ValueError("TOKEN NOT FOUND")

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    asyncio.create_task(
        background_reminder(bot)
    )

    app = web.Application()

    app['bot'] = bot

    app.router.add_post(
        "/webhook",
        handle_webhook
    )

    runner = web.AppRunner(app)

    await runner.setup()

    site = web.TCPSite(
        runner,
        "0.0.0.0",
        PORT
    )

    await site.start()

    await on_startup(bot)

    logging.info("✅ Noorify Bot Running")

    await asyncio.Event().wait()

# ============================================================
# تشغيل الملف
# ============================================================

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
