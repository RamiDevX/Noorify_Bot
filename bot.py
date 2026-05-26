# ============================================
# NoorifyBot - Islamic Reminder Telegram Bot
# Developer: Rami
# Library: aiogram 3
# ============================================

# تثبيت المكتبات:
# pip install aiogram apscheduler aiosqlite

# ============================================
# FILE: bot.py
# ============================================

import asyncio
import random
import aiosqlite
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ============================================
# CONFIG
# ============================================

TOKEN = "8632383100:AAHsR6l0sOQdI4FepaaRGOeW1WH1kJHWOcY"

BOT_USERNAME = "Noorify_Bot"
DEVELOPER = "@vx_rq"

# ============================================
# DATABASE
# ============================================

DB_PATH = "noorify.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                chat_id INTEGER PRIMARY KEY,
                interval_hours REAL,
                enabled INTEGER
            )
            """
        )
        await db.commit()

# ============================================
# 100 AZKAR + DUA + SHORT AYAT
# ============================================

AZKAR = [

    "سبحان الله وبحمده سبحان الله العظيم 🤍",
    "لا إله إلا الله وحده لا شريك له",
    "أستغفر الله العظيم وأتوب إليه",
    "اللهم صل وسلم على نبينا محمد ﷺ",
    "حسبي الله ونعم الوكيل",
    "لا حول ولا قوة إلا بالله",
    "اللهم اغفر لي ولوالدي",
    "اللهم ارزقنا الراحة والطمأنينة",
    "اللهم اجعل القرآن ربيع قلوبنا",
    "اللهم اهدنا الصراط المستقيم",
    "رب اغفر وارحم وأنت خير الراحمين",
    "رب زدني علمًا",
    "اللهم ثبت قلبي على دينك",
    "اللهم ارزقنا حسن الخاتمة",
    "اللهم اجعلنا من الذاكرين",
    "سبحان الله",
    "الحمد لله",
    "الله أكبر",
    "لا إله إلا الله",
    "سبحان الله والحمد لله",
    "سبحان الله العظيم",
    "اللهم إني أسألك الجنة",
    "اللهم أجرنا من النار",
    "اللهم ارزقنا الفردوس الأعلى",
    "اللهم فرج همومنا",
    "اللهم اشف مرضانا",
    "اللهم ارحم موتانا",
    "اللهم انصر المسلمين",
    "اللهم بارك لنا في أعمارنا",
    "اللهم ارزقنا التوفيق",
    "اللهم اجعلنا من الصالحين",
    "اللهم اغفر ذنوبنا",
    "اللهم ارزقنا رضاك",
    "اللهم ارزقنا السكينة",
    "اللهم لا تكلنا إلى أنفسنا",
    "اللهم ارزقنا حبك",
    "اللهم اجعلنا من المتقين",
    "اللهم ارزقنا الإخلاص",
    "اللهم تقبل منا صالح الأعمال",
    "اللهم اجعلنا من أهل القرآن",

    "﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنْفَعُ الْمُؤْمِنِينَ ﴾",
    "﴿ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ ﴾",
    "﴿ فَاذْكُرُونِي أَذْكُرْكُمْ ﴾",
    "﴿ وَاللَّهُ خَيْرُ الرَّازِقِينَ ﴾",
    "﴿ إِنَّ مَعَ الْعُسْرِ يُسْرًا ﴾",
    "﴿ وَتَوَكَّلْ عَلَى اللَّهِ ﴾",
    "﴿ رَبِّ زِدْنِي عِلْمًا ﴾",
    "﴿ وَاللَّهُ غَفُورٌ رَحِيمٌ ﴾",
    "﴿ إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ ﴾",
    "﴿ وَاصْبِرْ وَمَا صَبْرُكَ إِلَّا بِاللَّهِ ﴾",

    "اللهم يسر أمورنا",
    "اللهم ارزقنا البركة",
    "اللهم اجعل يومنا سعيدًا",
    "اللهم ارح قلوبنا",
    "اللهم أصلح أحوالنا",
    "اللهم اجعل لنا من كل هم فرجًا",
    "اللهم ارزقنا نورًا في قلوبنا",
    "اللهم اجعلنا من عبادك الصالحين",
    "اللهم ارزقنا راحة البال",
    "اللهم قربنا إليك",

    "سبحان الله عدد خلقه",
    "سبحان الله رضا نفسه",
    "سبحان الله زنة عرشه",
    "سبحان الله مداد كلماته",
    "الحمد لله دائمًا وأبدًا",
    "الله أكبر كبيرًا",
    "سبحان الله بكرة وأصيلًا",
    "اللهم صل على محمد",
    "اللهم سلمنا وسلم منا",
    "اللهم اكتب لنا الخير",

    "اللهم اجعلنا من التوابين",
    "اللهم اجعلنا من المتطهرين",
    "اللهم ارزقنا القناعة",
    "اللهم ارحم ضعفنا",
    "اللهم اغفر لنا تقصيرنا",
    "اللهم ارزقنا الصبر",
    "اللهم ارزقنا الثبات",
    "اللهم اجعلنا من الشاكرين",
    "اللهم ارزقنا حسن الظن بك",
    "اللهم لا تحرمنا فضلك",

    "﴿ إِنَّ اللَّهَ يُحِبُّ التَّوَّابِينَ ﴾",
    "﴿ وَرَحْمَتِي وَسِعَتْ كُلَّ شَيْءٍ ﴾",
    "﴿ وَاللَّهُ يُحِبُّ الصَّابِرِينَ ﴾",
    "﴿ وَاللَّهُ خَيْرٌ وَأَبْقَىٰ ﴾",
    "﴿ وَاللَّهُ سَمِيعٌ عَلِيمٌ ﴾",
    "﴿ وَاللَّهُ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ ﴾",
    "﴿ إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ ﴾",
    "﴿ وَاللَّهُ يُحِبُّ الْمُتَّقِينَ ﴾",
    "﴿ وَاصْبِرُوا إِنَّ اللَّهَ مَعَ الصَّابِرِينَ ﴾",
    "﴿ وَإِلَى اللَّهِ تُرْجَعُ الْأُمُورُ ﴾",

    "اللهم ارزقنا السعادة",
    "اللهم اجعلنا من أهل الجنة",
    "اللهم انفعنا بما علمتنا",
    "اللهم علمنا ما ينفعنا",
    "اللهم اكتب لنا الأجر",
    "اللهم ارزقنا حب الخير",
    "اللهم اجعل القرآن نورًا لنا",
    "اللهم اجعلنا من عبادك المخلصين",
    "اللهم ارزقنا راحة القلب",
    "اللهم اجعل لنا نصيبًا من الرحمة",

    "سبحان الله العظيم وبحمده",
    "الحمد لله رب العالمين",
    "اللهم لك الحمد كله",
    "اللهم ارزقنا التوبة النصوح",
    "اللهم اجعل أعمالنا خالصة لوجهك",
    "اللهم اهد شباب المسلمين",
    "اللهم ارزقنا الطمأنينة",
    "اللهم احفظ أهلنا",
    "اللهم بارك لنا في أيامنا",
    "اللهم اكتب لنا الخير أينما كان"

]

# ============================================
# SMART ALGORITHM
# ============================================

last_sent = {}

def get_smart_zekr(chat_id):

    if chat_id not in last_sent:
        last_sent[chat_id] = []

    used = last_sent[chat_id]

    available = [z for z in AZKAR if z not in used]

    if not available:
        last_sent[chat_id] = []
        available = AZKAR.copy()

    zekr = random.choice(available)

    last_sent[chat_id].append(zekr)

    if len(last_sent[chat_id]) > 15:
        last_sent[chat_id].pop(0)

    return zekr

# ============================================
# BOT
# ============================================

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

scheduler = AsyncIOScheduler()

# ============================================
# KEYBOARDS
# ============================================
def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[

            # الصف 1
            [
                InlineKeyboardButton(
                    text="➕ إضافة للمجموعة",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
                InlineKeyboardButton(
                    text="📢 إضافة للقناة",
                    url=f"https://t.me/{BOT_USERNAME}?startchannel=true"
                )
            ],

            # الصف 2
            [
                InlineKeyboardButton(
                    text="📤 مشاركة البوت",
                    switch_inline_query=f"جربوا {BOT_USERNAME} 🤍"
                ),
                InlineKeyboardButton(
                    text="⏰ الضبط الدوري",
                    callback_data="schedule"
                )
            ],

            # الصف 3
            [
                InlineKeyboardButton(
                    text="✅ تفعيل الأذكار",
                    callback_data="enable"
                ),
                InlineKeyboardButton(
                    text="❌ إلغاء الأذكار",
                    callback_data="disable"
                )
            ],

            # الصف الأخير (زر واحد فقط)
            [
                InlineKeyboardButton(
                    text="👨‍💻 مطور البوت",
                    url=f"https://t.me/{DEVELOPER.lstrip('@')}"
                )
            ]
        ]
    )
# ============================================
# SCHEDULE MENU
# ============================================

def schedule_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="30 دقيقة",
                    callback_data="time_0.5"
                ),

                InlineKeyboardButton(
                    text="1 ساعة",
                    callback_data="time_1"
                )
            ],

            [
                InlineKeyboardButton(
                    text="2 ساعات",
                    callback_data="time_2"
                ),

                InlineKeyboardButton(
                    text="3 ساعات",
                    callback_data="time_3"
                )
            ],

            [
                InlineKeyboardButton(
                    text="6 ساعات",
                    callback_data="time_6"
                ),

                InlineKeyboardButton(
                    text="12 ساعة",
                    callback_data="time_12"
                )
            ],

            [
                InlineKeyboardButton(
                    text="يومي",
                    callback_data="time_24"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔙 رجوع",
                    callback_data="back"
                )
            ]
        ]
    )

# ============================================
# SEND REMINDER
# ============================================

async def get_chat_enabled(chat_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT enabled FROM reminders WHERE chat_id=?",
            (chat_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if not row:
                return 0
            return int(row[0])


async def send_reminder(chat_id: int):
    enabled = await get_chat_enabled(chat_id)
    if enabled == 0:
        return

    zekr = get_smart_zekr(chat_id)

    text = f"""
📿 <b>تذكير إيماني</b>

{zekr}

🤍 NoorifyBot
"""

    try:
        await bot.send_message(chat_id, text)
    except Exception:
        # لا نوقف البوت إذا فشل الإرسال لسبب مؤقت
        return

# ============================================
# START
# ============================================

WELCOME = """
السلام عليكم 🌸

أهلاً بك في NoorifyBot 🤍

بوت للتذكير بالأذكار والأدعية والآيات القصيرة.

﴿ وَذَكِّرْ فَإِنَّ الذِّكْرَىٰ تَنْفَعُ الْمُؤْمِنِينَ ﴾

ابدأ من الأزرار بالأسفل 👇
"""
@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        WELCOME,
        reply_markup=main_menu()
    )


@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):

    await callback.message.edit_text(
        WELCOME,
        reply_markup=main_menu()
    )
@dp.callback_query(F.data == "schedule")
async def schedule(callback: CallbackQuery):

    await callback.message.edit_reply_markup(
        reply_markup=schedule_menu()
    )

@dp.callback_query(F.data.startswith("time_"))
async def set_time(callback: CallbackQuery):
    hours = float(callback.data.split("_")[1])
    chat_id = callback.message.chat.id
    job_id = str(chat_id)

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO reminders
            (chat_id, interval_hours, enabled)
            VALUES (?, ?, ?)
            """,
            (chat_id, hours, 1)
        )
        await db.commit()

    # تحديث الـ job بشكل آمن
    try:
        scheduler.remove_job(job_id)
    except Exception:
        pass

    scheduler.add_job(
        send_reminder,
        "interval",
        hours=hours,
        args=[chat_id],
        id=job_id,
        replace_existing=True,
    )

    await callback.answer("تم ضبط التذكير بنجاح ✅")


async def get_interval_hours(chat_id: int) -> float | None:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT interval_hours FROM reminders WHERE chat_id=?",
            (chat_id,)
        ) as cur:
            row = await cur.fetchone()
            if not row:
                return None
            return row[0]


@dp.callback_query(F.data == "enable")
async def enable(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    job_id = str(chat_id)

    # تحسين enable: إعادة استخدام interval_hours السابق من DB
    hours = await get_interval_hours(chat_id)
    if hours is None:
        hours = 6

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO reminders
            (chat_id, interval_hours, enabled)
            VALUES (?, COALESCE((SELECT interval_hours FROM reminders WHERE chat_id=?), ?), ?)
            """,
            (chat_id, chat_id, hours, 1)
        )
        await db.commit()

    try:
        scheduler.remove_job(job_id)
    except Exception:
        pass

    scheduler.add_job(
        send_reminder,
        "interval",
        hours=float(hours),
        args=[chat_id],
        id=job_id,
        replace_existing=True,
    )

    await callback.answer("تم تفعيل الأذكار ✅")


@dp.callback_query(F.data == "disable")
async def disable(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    job_id = str(chat_id)

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            UPDATE reminders
            SET enabled=0
            WHERE chat_id=?
            """,
            (chat_id,)
        )
        await db.commit()

    try:
        scheduler.remove_job(job_id)
    except Exception:
        pass

    await callback.answer("تم إلغاء الأذكار ❌")


# ============================================
# STARTUP
# ============================================

async def load_jobs():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT chat_id, interval_hours FROM reminders WHERE enabled=1"
        ) as cur:
            rows = await cur.fetchall()

    for chat_id, hours in rows:
        if hours is None:
            continue
        job_id = str(chat_id)
        try:
            scheduler.remove_job(job_id)
        except Exception:
            pass

        scheduler.add_job(
            send_reminder,
            "interval",
            hours=float(hours),
            args=[chat_id],
            id=job_id,
            replace_existing=True,
        )


async def main():
    await init_db()
    scheduler.start()
    await load_jobs()

    print("NoorifyBot Started Successfully")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
