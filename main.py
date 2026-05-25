```python
import asyncio
import random
import logging
import sys
import time
import os

from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, Any, Union

from aiogram import Bot, Dispatcher, F, html
from aiogram.filters import Command, ChatMemberUpdatedFilter
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
    ChatMemberUpdated,
    BotCommand,
    Update
)

from aiogram.enums import ParseMode, ChatMemberStatus
from aiogram.client.default import DefaultBotProperties
from aiohttp import web

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# CONFIG
# ==========================================

TOKEN = os.getenv("TOKEN")

MY_USER_ID = 1408037752

MY_GROUP_ID = -1003650088178

DEVELOPER_USERNAME = "vx_rq"

DEVELOPER_URL = "https://t.me/vx_rq"

TECH_CHANNEL = "https://t.me/RamiAILab"

BOT_NAME = "NOORIFY BOT ✨"

PORT = int(os.getenv("PORT", 8080))

WEBHOOK_HOST = os.getenv(
    "WEBHOOK_HOST",
    "https://noorify-bot.onrender.com"
)

WEBHOOK_PATH = "/webhook"

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# ==========================================
# BOT
# ==========================================

dp = Dispatcher()

# ==========================================
# DATABASE
# ==========================================

active_chats: Dict[int, Dict[str, Any]] = {}

user_db: Dict[int, Dict[str, Any]] = {}

LANGS = {}

# ==========================================
# LANGUAGES
# ==========================================

TEXTS = {
    "ar": {

        "welcome":
"""
🌙 أهلاً بك في بوت نُورِفَاي الإسلامي ✨

📿 أذكار وأدعية ومسبحة إلكترونية
🕌 تذكيرات إيمانية احترافية
💎 تصميم عصري وتجربة فريدة

اختر ما تريد من القائمة بالأسفل 👇
""",

        "tasbih": "📿 المسبحة",
        "random": "✨ ذكر عشوائي",
        "stats": "📊 إحصائياتي",
        "settings": "⚙️ الإعدادات",
        "back": "🔙 رجوع",
        "developer": "👨🏻‍💻 المطور",
        "channel": "📢 القناة التقنية",
        "share": "🔗 مشاركة البوت",
        "add_group": "➕ إضافة لمجموعة",
        "add_channel": "📡 إضافة لقناة",
        "language": "🌐 اللغة",
        "contact": "💬 التواصل",
        "tasbih_choose": "اختر نوع التسبيح 👇",
        "random_title": "✨ ذكر اليوم",
        "stats_title": "📊 إحصائياتك",
    },

    "tr": {

        "welcome":
"""
🌙 Noorify İslami Bota Hoş Geldiniz ✨

📿 Zikirler, dualar ve elektronik tesbih
🕌 Profesyonel manevi hatırlatmalar
💎 Modern ve şık deneyim

Aşağıdaki menüden seçim yapın 👇
""",

        "tasbih": "📿 Tesbih",
        "random": "✨ Rastgele Zikir",
        "stats": "📊 İstatistiklerim",
        "settings": "⚙️ Ayarlar",
        "back": "🔙 Geri",
        "developer": "👨🏻‍💻 Geliştirici",
        "channel": "📢 Teknoloji Kanalı",
        "share": "🔗 Botu Paylaş",
        "add_group": "➕ Gruba Ekle",
        "add_channel": "📡 Kanala Ekle",
        "language": "🌐 Dil",
        "contact": "💬 İletişim",
        "tasbih_choose": "Tesbih türünü seç 👇",
        "random_title": "✨ Günlük Zikir",
        "stats_title": "📊 İstatistikler",
    }
}

# ==========================================
# ADHKAR
# ==========================================

ADHKAR_LIST = [

    "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",

    "لَا إِلَهَ إِلَّا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ",

    "رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي",

    "اللهم اجعل القرآن ربيع قلوبنا ونور صدورنا",

    "اللهم ثبتنا على دينك حتى نلقاك",

    "اللهم ارزقنا حسن الخاتمة",

    "سبحان الله وبحمده سبحان الله العظيم",

    "لا حول ولا قوة إلا بالله",

    "اللهم صل وسلم على نبينا محمد",

    "أستغفر الله العظيم وأتوب إليه",

    "اللهم إني توكلت عليك فأعنّي",

    "اللهم افتح لنا أبواب رحمتك",

    "يا رب اشرح صدورنا بالإيمان",

    "اللهم اجعلنا من الذاكرين الشاكرين",

    "اللهم ارزقنا راحة البال وطمأنينة القلب",

    "اللهم اغفر لنا ولوالدينا ولجميع المسلمين",

    "يا حي يا قيوم برحمتك أستغيث",

    "ومن يتوكل على الله فهو حسبه",

    "إن مع العسر يسرا",

    "سلام قولاً من رب رحيم",

    "الله نور السماوات والأرض",

    "اللهم اجعلنا من أهل الجنة",

    "ما شاء الله لا قوة إلا بالله",

    "اللهم اكفني بحلالك عن حرامك",

    "اللهم إني أعوذ بك من الهم والحزن",

    "اللهم ارزقني رزقاً طيباً مباركاً فيه",

    "سبحان الله عدد خلقه ورضا نفسه",

    "اللهم اجعل أعمالنا خالصة لوجهك الكريم",

    "لا إله إلا الله الملك الحق المبين",

    "اللهم اجعل في قلبي نوراً",

]

# ==========================================
# TASBIH TYPES
# ==========================================

TASBIH_TYPES = [

    "🟢 سبحان الله",
    "⚪ الحمد لله",
    "🟡 لا إله إلا الله",
    "🟠 الله أكبر",
    "🔴 أستغفر الله",
    "🔵 صلّ على محمد",
    "🟣 لا حول ولا قوة إلا بالله",
    "🟤 سبحان الله وبحمده",
    "⚫ سبحان الله العظيم",
    "🟢 يا حي يا قيوم",
]

# ==========================================
# HELPERS
# ==========================================

def get_lang(user_id):

    return LANGS.get(user_id, "ar")


def t(user_id, key):

    lang = get_lang(user_id)

    return TEXTS[lang].get(key, key)


def init_user(uid: int, name: str):

    if uid not in user_db:

        user_db[uid] = {
            "name": name,
            "tasbih": 0,
            "join_date": datetime.now().strftime("%Y/%m/%d"),
        }

    return user_db[uid]


def get_progress(current: int, limit: int = 33):

    slots = 12

    filled = int((min(current, limit) / limit) * slots)

    bar = "◈" * filled + "◇" * (slots - filled)

    return f"【 {bar} 】"


def get_rank(total: int):

    if total >= 2500:
        return "ذاكر مخلص 🕊️"

    elif total >= 1000:
        return "ذاكر مستمر 🌟"

    elif total >= 500:
        return "محب للخير 🌿"

    elif total >= 100:
        return "ساعٍ للبر 🐚"

    return "مبتدئ 🕊️"


def text_welcome(user_id: int):

    lang = get_lang(user_id)

    return (
        f"{TEXTS[lang]['welcome']}\n"
        f"━━━━━━━━━━━━━━━\n"
        f"🕋 {BOT_NAME}\n"
        f"✨ Islamic Smart Experience\n"
        f"━━━━━━━━━━━━━━━"
    )

# ==========================================
# MAIN KEYBOARD
# ==========================================

def kb_main(user_id: int, username: str):

    return InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text=t(user_id, "tasbih"),
                    callback_data="btn_tasbih_menu"
                ),

                InlineKeyboardButton(
                    text=t(user_id, "random"),
                    callback_data="btn_random"
                )
            ],

            [
                InlineKeyboardButton(
                    text=t(user_id, "stats"),
                    callback_data="btn_stats"
                ),

                InlineKeyboardButton(
                    text=t(user_id, "settings"),
                    callback_data="btn_settings"
                )
            ],

            [
                InlineKeyboardButton(
                    text=t(user_id, "channel"),
                    url=TECH_CHANNEL
                )
            ],

            [
                InlineKeyboardButton(
                    text=t(user_id, "developer"),
                    url=DEVELOPER_URL
                ),

                InlineKeyboardButton(
                    text=t(user_id, "contact"),
                    url=DEVELOPER_URL
                )
            ],

            [
                InlineKeyboardButton(
                    text=t(user_id, "share"),
                    url=f"https://t.me/share/url?url=https://t.me/{username}"
                )
            ],

            [
                InlineKeyboardButton(
                    text=t(user_id, "add_group"),
                    url=f"https://t.me/{username}?startgroup=true"
                ),

                InlineKeyboardButton(
                    text=t(user_id, "add_channel"),
                    url=f"https://t.me/{username}?startchannel=true"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🇸🇦 العربية",
                    callback_data="lang_ar"
                ),

                InlineKeyboardButton(
                    text="🇹🇷 Türkçe",
                    callback_data="lang_tr"
                )
            ]
        ]
    )

# ==========================================
# ADMIN CHECK
# ==========================================

async def is_admin(event: Union[Message, CallbackQuery]):

    uid = event.from_user.id

    if uid == MY_USER_ID:
        return True

    chat = event.message.chat if isinstance(
        event,
        CallbackQuery
    ) else event.chat

    if chat.type == "private":
        return True

    try:

        member = await event.bot.get_chat_member(
            chat.id,
            uid
        )
return member.status in [
    ChatMemberStatus.ADMINISTRATOR,
    ChatMemberStatus.OWNER
]
    except:

        return False

# ==========================================
# START
# ==========================================

@dp.message(Command("start"))
async def cmd_start(message: Message):

    init_user(
        message.from_user.id,
        message.from_user.full_name
    )

    bot_info = await message.bot.get_me()

    await message.answer(

        text=text_welcome(message.from_user.id),

        reply_markup=kb_main(
            message.from_user.id,
            bot_info.username
        ),

        parse_mode="HTML"
    )

# ==========================================
# HELP
# ==========================================

@dp.message(Command("help"))
async def cmd_help(message: Message):

    await message.answer(
        f"""
🆘 HELP MENU

👨🏻‍💻 Developer:
{DEVELOPER_URL}

📢 Channel:
{TECH_CHANNEL}

✨ Use /start to return
"""
    )

# ==========================================
# LANGUAGE
# ==========================================

@dp.callback_query(F.data.startswith("lang_"))
async def change_language(call: CallbackQuery):

    lang = call.data.split("_")[1]

    LANGS[call.from_user.id] = lang

    bot_info = await call.bot.get_me()

    await call.message.edit_text(

        text_welcome(call.from_user.id),

        reply_markup=kb_main(
            call.from_user.id,
            bot_info.username
        ),

        parse_mode="HTML"
    )

# ==========================================
# TASBIH MENU
# ==========================================

@dp.callback_query(F.data == "btn_tasbih_menu")
async def btn_tasbih_menu(call: CallbackQuery):

    keyboard = []

    row = []

    for i, item in enumerate(TASBIH_TYPES):

        row.append(
            InlineKeyboardButton(
                text=item,
                callback_data=f"go_{i}"
            )
        )

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append([

        InlineKeyboardButton(
            text=t(call.from_user.id, "back"),
            callback_data="btn_home"
        )
    ])

    await call.message.edit_text(

        t(call.from_user.id, "tasbih_choose"),

        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=keyboard
        )
    )

# ==========================================
# TASBIH ENGINE
# ==========================================

@dp.callback_query(F.data.startswith(("go_", "hit_")))
async def tasbih_engine(call: CallbackQuery):

    idx = int(call.data.split("_")[1])

    user = init_user(
        call.from_user.id,
        call.from_user.full_name
    )

    if call.data.startswith("hit_"):

        user["tasbih"] += 1

    progress = get_progress(
        user["tasbih"] % 33
    )

    rank = get_rank(user["tasbih"])

    keyboard = InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="✨ اضغط للتسبيح ✨",
                    callback_data=f"hit_{idx}"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔄 تغيير",
                    callback_data="btn_tasbih_menu"
                ),

                InlineKeyboardButton(
                    text="🔙 رجوع",
                    callback_data="btn_home"
                )
            ]
        ]
    )

    text = f"""
📿 {TASBIH_TYPES[idx]}

━━━━━━━━━━━━━━━

📊 التقدم:
{progress}

🏅 الرتبة:
{rank}

📿 العدد:
{user['tasbih']}

━━━━━━━━━━━━━━━
✨ استمر في الذكر
"""

    await call.message.edit_text(
        text,
        reply_markup=keyboard
    )

# ==========================================
# RANDOM DHIKR
# ==========================================

@dp.callback_query(F.data == "btn_random")
async def btn_random(call: CallbackQuery):

    dhikr = random.choice(ADHKAR_LIST)

    keyboard = InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🔄 ذكر آخر",
                    callback_data="btn_random"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔙 رجوع",
                    callback_data="btn_home"
                )
            ]
        ]
    )

    await call.message.edit_text(

        f"""
✨ {t(call.from_user.id, 'random_title')}

╭──────────────╮

{html.code(dhikr)}

╰──────────────╯

🕊️ نور لقلبك
🌙 وطمأنينة لروحك
""",

        parse_mode="HTML",

        reply_markup=keyboard
    )

# ==========================================
# STATS
# ==========================================

@dp.callback_query(F.data == "btn_stats")
async def btn_stats(call: CallbackQuery):

    user = init_user(
        call.from_user.id,
        call.from_user.full_name
    )

    text = f"""
📊 {t(call.from_user.id, 'stats_title')}

━━━━━━━━━━━━━━━

👤 الاسم:
{user['name']}

🏅 الرتبة:
{get_rank(user['tasbih'])}

📿 إجمالي التسبيحات:
{user['tasbih']}

📅 تاريخ الانضمام:
{user['join_date']}

━━━━━━━━━━━━━━━
✨ بارك الله فيك
"""

    await call.message.edit_text(

        text,

        reply_markup=InlineKeyboardMarkup(

            inline_keyboard=[

                [
                    InlineKeyboardButton(
                        text="🔙 رجوع",
                        callback_data="btn_home"
                    )
                ]
            ]
        )
    )

# ==========================================
# SETTINGS
# ==========================================

@dp.callback_query(F.data == "btn_settings")
async def btn_settings(call: CallbackQuery):

    if not await is_admin(call):

        return await call.answer(
            "❌ للمشرفين فقط",
            show_alert=True
        )

    keyboard = InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="30m",
                    callback_data="set_0.5"
                ),

                InlineKeyboardButton(
                    text="1h",
                    callback_data="set_1"
                )
            ],

            [
                InlineKeyboardButton(
                    text="3h",
                    callback_data="set_3"
                ),

                InlineKeyboardButton(
                    text="6h",
                    callback_data="set_6"
                )
            ],

            [
                InlineKeyboardButton(
                    text="12h",
                    callback_data="set_12"
                ),

                InlineKeyboardButton(
                    text="24h",
                    callback_data="set_24"
                )
            ],

            [
                InlineKeyboardButton(
                    text="❌ إيقاف",
                    callback_data="set_off"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔙 رجوع",
                    callback_data="btn_home"
                )
            ]
        ]
    )

    await call.message.edit_text(

        "⚙️ إعدادات التذكير الدوري",

        reply_markup=keyboard
    )

# ==========================================
# SAVE SETTINGS
# ==========================================

@dp.callback_query(F.data.startswith("set_"))
async def save_settings(call: CallbackQuery):

    if not await is_admin(call):
        return

    value = call.data.split("_")[1]

    chat_id = call.message.chat.id

    if value == "off":

        active_chats.pop(chat_id, None)

        await call.answer(
            "✅ تم الإيقاف",
            show_alert=True
        )

    else:

        active_chats[chat_id] = {

            "interval": float(value),
            "last": time.time()
        }

        await call.answer(
            f"✅ تم التفعيل كل {value} ساعة",
            show_alert=True
        )

    await back_home(call)

# ==========================================
# BACK HOME
# ==========================================

@dp.callback_query(F.data == "btn_home")
async def back_home(call: CallbackQuery):

    bot_info = await call.bot.get_me()

    await call.message.edit_text(

        text_welcome(call.from_user.id),

        reply_markup=kb_main(
            call.from_user.id,
            bot_info.username
        ),

        parse_mode="HTML"
    )

# ==========================================
# BROADCAST
# ==========================================

@dp.message(Command("broadcast"))
async def broadcast(message: Message):

    if message.from_user.id != MY_USER_ID:
        return

    text = message.text.replace(
        "/broadcast",
        ""
    ).strip()

    if not text:

        return await message.reply(
            "اكتب الرسالة بعد الأمر."
        )

    sent = 0

    failed = 0

    wait = await message.reply(
        "🚀 بدء البث الذكي..."
    )

    for uid in list(user_db.keys()):

        try:

            await message.bot.send_message(

                uid,

                f"""
📢 رسالة جديدة من إدارة البوت

{text}

━━━━━━━━━━━━━━━
✨ شكراً لاستخدامك {BOT_NAME}
""",

                parse_mode="HTML"
            )

            sent += 1

            await asyncio.sleep(0.05)

        except:

            failed += 1

    await wait.edit_text(

        f"""
✅ اكتمل البث

📨 تم الإرسال:
{sent}

❌ فشل:
{failed}
"""
    )

# ==========================================
# BOT JOIN
# ==========================================

@dp.my_chat_member()
async def on_bot_join(event: ChatMemberUpdated):

    if event.new_chat_member.status not in [
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR
    ]:
        return

    try:

        await event.bot.send_message(
            event.chat.id,
            f"""
🎉 تم تفعيل {BOT_NAME}

📿 سيتم نشر الأذكار والتذكيرات

⚙️ يمكن للمشرفين تعديل الإعدادات
""",
            parse_mode="HTML"
        )

    except Exception:
        pass
# ==========================================
# AUTO BROADCASTER
# ==========================================

async def background_broadcaster(bot: Bot):

    while True:

        now = time.time()

        for chat_id, config in list(active_chats.items()):

            if now - config["last"] >= (
                config["interval"] * 3600
            ):

                try:

                    dhikr = random.choice(
                        ADHKAR_LIST
                    )

                    await bot.send_message(

                        chat_id,

                        f"""
💠 نفحات نُورِفَاي

{html.code(dhikr)}

✨ لا تنس ذكر الله
""",

                        parse_mode="HTML"
                    )

                    active_chats[chat_id]["last"] = now

                except:

                    active_chats.pop(chat_id, None)

        await asyncio.sleep(60)

# ==========================================
# WEBHOOK
# ==========================================

async def handle_webhook(request: web.Request):

    try:

        bot: Bot = request.app["bot"]

        data = await request.json()

        update = Update(**data)

        await dp.feed_update(bot, update)

    except Exception as e:

        logging.error(e)

    return web.Response(text="OK")

# ==========================================
# STARTUP
# ==========================================

async def on_startup(bot: Bot):

    await bot.delete_webhook(
        drop_pending_updates=True
    )

    await asyncio.sleep(1)

    await bot.set_webhook(
        WEBHOOK_URL
    )

    print("✅ Webhook Connected")

# ==========================================
# SHUTDOWN
# ==========================================

async def on_shutdown(bot: Bot):

    await bot.delete_webhook()

# ==========================================
# MAIN
# ==========================================

async def main():

    bot = Bot(

        token=TOKEN,

        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    asyncio.create_task(
        background_broadcaster(bot)
    )

    await bot.set_my_commands([

        BotCommand(
            command="start",
            description="🌙 تشغيل البوت"
        ),

        BotCommand(
            command="help",
            description="🆘 المساعدة"
        ),

        BotCommand(
            command="broadcast",
            description="📢 بث للمطور"
        ),
    ])

    await on_startup(bot)

    app = web.Application()

    app["bot"] = bot

    app.router.add_post(
        WEBHOOK_PATH,
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

    print(f"🚀 {BOT_NAME} RUNNING")

    try:

        await asyncio.Event().wait()

    except KeyboardInterrupt:

        await on_shutdown(bot)

        await runner.cleanup()

# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout
    )

    try:

        asyncio.run(main())

    except (
        KeyboardInterrupt,
        SystemExit
    ):

        pass
```
