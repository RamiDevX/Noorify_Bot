import asyncio
import random
import logging
import sys
import time
import re
import os
from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, Any, List, Union, Optional

# تحميل المتغيرات من ملف .env
load_dotenv()

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
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from aiohttp import web

# --- [ الإعدادات العليا للنظام الملكي ] ---
TOKEN = os.getenv("TOKEN")
MY_USER_ID = 1408037752
MY_GROUP_ID = -1003650088178
DEVELOPER_URL = "https://t.me/vx_rq"
TECH_CHANNEL = "https://t.me/RamiAILab"

# إعدادات Render و Webhook
PORT = int(os.getenv("PORT", 8080))
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://noorify-bot.onrender.com")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

dp = Dispatcher()

# --- [ قاعدة البيانات العملاقة - أضخم قائمة أذكار غير مختصرة ] ---
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

active_chats: Dict[int, Dict[str, Any]] = {}
user_db: Dict[int, Dict[str, Any]] = {}

def get_unique_progress(current: int, limit: int = 33) -> str:
    slots = 12
    filled = int((min(current, limit) / limit) * slots)
    bar = "◈" * filled + "◇" * (slots - filled)
    return f"【 {bar} 】 ⚡ {int((current/limit)*100)}%"

async def is_admin(event: Union[Message, CallbackQuery]) -> bool:
    uid = event.from_user.id
    if uid == MY_USER_ID: return True
    chat = event.message.chat if isinstance(event, CallbackQuery) else event.chat
    if chat.type == "private": return True
    try:
        m = await event.bot.get_chat_member(chat.id, uid)
        return m.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER, ChatMemberStatus.CREATOR]
    except: return False

def init_user(uid: int, name: str) -> Dict[str, Any]:
    if uid not in user_db:
        user_db[uid] = {
            "name": name, 
            "tasbih": 0, 
            "level": 1,
            "join_date": datetime.now().strftime("%Y/%m/%d %I:%M %p"),
            "achievements": [],
            "points": 0
        }
    return user_db[uid]

def get_spiritual_rank(total: int) -> tuple:
    ranks = [
        (2500, "ذاكر مخلص 🕊️", "🛡️"),
        (1000, "ذاكر مستمر 🌟", "🌟"),
        (500, "مُحب للخير 🌱", "🌿"),
        (100, "ساعٍ للبر 🐚", "🐚"),
        (0, "مجاهد مبتدئ 🕊️", "🕊️")
    ]
    for limit, title, icon in ranks:
        if total >= limit: return title, icon
    return ranks[-1][1], ranks[-1][2]

def ai_spiritual_analysis(total: int) -> str:
    if total == 0: return "اللَّهُمَّ تَقَبَّلْ مِنْكَ."
    if total < 100: return "بَارَكَ اللهُ فِيكَ وَنَفَعَ بِكَ."
    if total < 1000: return "فِي مِيزَانِ حَسَنَاتِكَ."
    if total < 2500: return "🌟 أَنتَ عَلَى طَرِيقِ الصَّلَاحِ."
    return "✨ بَارِكَ اللهُ فِيكَ دَاخِلَ الجَنَّة."

def text_welcome() -> str:
    return (
        "🌟 مَرْحَبًا بِكَ فِي نُورِفَاي 🌟\n"
        "🕊️ بوت الأذكار والأدعية الإسلامية\n\n"
        "اختر ما تريد:\n"
        "📿 استخدم المسبحة الإلكترونية\n"
        "✨ احصل على ذكر عشوائي\n"
        "📊 شاهد إحصائياتك\n"
        f"👨‍💻 {html.link('تطوير البوت', DEVELOPER_URL)}"
    )

def kb_main(username: str = None) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📿 المسبحة", callback_data="btn_tasbih_menu")],
        [InlineKeyboardButton(text="✨ ذكر عشوائي", callback_data="btn_random")],
        [InlineKeyboardButton(text="📊 الإحصائيات", callback_data="btn_stats")],
        [InlineKeyboardButton(text="⚙️ الضبط الدوري", callback_data="btn_settings")],
    ])

# --- [ معالجات الأوامر الأساسية ] ---
@dp.message(Command("start"))
async def cmd_start(message: Message):
    bot_info = await message.bot.get_me()
    init_user(message.from_user.id, message.from_user.full_name)
    await message.answer(text=text_welcome(), reply_markup=kb_main(bot_info.username), parse_mode="HTML")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        f"🆘 المساعدة\n\n"
        f"👨‍💻 المبرمج: {html.link('vx_rq', DEVELOPER_URL)}\n"
        f"📢 القناة: {html.link('RamiAILab', TECH_CHANNEL)}\n\n"
        f"استخدم /start للعودة للقائمة الرئيسية",
        parse_mode="HTML"
    )

@dp.message(Command("guide"))
async def cmd_guide(message: Message):
    await message.answer(
        "📑 دليل الاستخدام:\n\n"
        "1. /start - فتح القائمة الرئيسية\n"
        "2. اضغط على 📿 المسبحة لبدء الذكر\n"
        "3. استخدم ✨ لذكر عشوائي\n"
        "4. اعرض إحصائياتك في 📊\n"
        "5. في المجموعات، استخدم ⚙️ لتفعيل الأذكار التلقائية"
    )

@dp.message(Command("broadcast"))
async def broadcast_message(message: Message):
    if message.from_user.id != MY_USER_ID:
        return await message.answer("❌ عذراً، هذه الميزة للمطور فقط.")
    broadcast_text = message.text.replace("/broadcast", "").strip()
    if not broadcast_text and not message.reply_to_message:
        return await message.answer("⚠️ يرجى كتابة النص المراد إرساله أو الرد على رسالة.")
    target_text = broadcast_text or message.reply_to_message.text
    msg = await message.answer("⏳ جاري الإرسال للجميع... 0%")
    success = 0
    failed = 0
    total = len(user_db)
    for index, user_id in enumerate(user_db.keys()):
        try:
            await message.bot.send_message(user_id, target_text, parse_mode="HTML")
            success += 1
            if index % 10 == 0:
                await msg.edit_text(f"⏳ جاري الإرسال... {int((index/total)*100) if total > 0 else 100}%")
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1
    await msg.edit_text(f"✅ تم الإرسال بنجاح!\n\n📨 ناجح: {success}\n❌ فشل: {failed}")

# --- [ معالجات القوائم ] ---
@dp.callback_query(F.data == "btn_tasbih_menu")
async def btn_tasbih_menu(call: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t, callback_data=f"go_{i}") for i, t in enumerate(TASBIH_TYPES[:2])],
        [InlineKeyboardButton(text=t, callback_data=f"go_{i+2}") for i, t in enumerate(TASBIH_TYPES[2:4])],
        [InlineKeyboardButton(text=t, callback_data=f"go_{i+4}") for i, t in enumerate(TASBIH_TYPES[4:6])],
        [InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")]
    ])
    await call.message.edit_text("اختر نوع التسبيح:", reply_markup=kb)

@dp.callback_query(F.data.startswith(("go_", "hit_")))
async def engine_tasbih(call: CallbackQuery):
    try:
        idx = int(call.data.split("_")[1])
    except (IndexError, ValueError):
        await call.answer("خطأ في البيانات", show_alert=True)
        return
    u = init_user(call.from_user.id, call.from_user.full_name)
    u.setdefault("tasbih", 0)
    if call.data.startswith("hit_"):
        u["tasbih"] += 1
    rank_n, rank_i = get_spiritual_rank(u["tasbih"])
    progress = get_unique_progress(u["tasbih"] % 34)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="اضغط هنا ✨", callback_data=f"hit_{idx}")],
        [
            InlineKeyboardButton(text="🔄 تغيير", callback_data="btn_tasbih_menu"),
            InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")
        ]
    ])
    txt = (
        f"{html.bold('المسبحة')} {rank_i}\n"
        f"🕊️ {html.italic(TASBIH_TYPES[idx])}\n\n"
        f"📊 التقدم: {html.code(progress)}\n"
        f"🏅 الرتبة: {rank_n}\n"
        f"📿 إجمالي: {u['tasbih']}\n"
    )
    try:
        await call.message.edit_text(txt, reply_markup=kb, parse_mode="HTML")
    except Exception:
        pass

@dp.callback_query(F.data == "btn_stats")
async def btn_stats_call(call: CallbackQuery):
    u = init_user(call.from_user.id, call.from_user.full_name)
    rank_n, rank_i = get_spiritual_rank(u['tasbih'])
    txt = (
        f"📊 {html.bold('الإحصائيات')} {rank_i}\n"
        f"👤 الاسم: {u['name']}\n"
        f"🏅 الرتبة: {rank_n}\n"
        f"📿 رصيد الأذكار: {html.bold(str(u['tasbih']))}\n"
        f"📅 التاريخ: {u['join_date']}\n\n"
        f"✨ {ai_spiritual_analysis(u['tasbih'])}\n"
    )
    await call.message.edit_text(txt, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔙 العودة", callback_data="btn_home")]]), parse_mode="HTML")

@dp.callback_query(F.data == "btn_settings")
async def btn_settings_callback(call: CallbackQuery):
    if not await is_admin(call):
        return await call.answer("❌ للمشرفين فقط", show_alert=True)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="30 دقيقة", callback_data="set_0.5"), InlineKeyboardButton(text="ساعة", callback_data="set_1")],
        [InlineKeyboardButton(text="3 ساعات", callback_data="set_3"), InlineKeyboardButton(text="6 ساعات", callback_data="set_6")],
        [InlineKeyboardButton(text="12 ساعة", callback_data="set_12"), InlineKeyboardButton(text="يومي", callback_data="set_24")],
        [InlineKeyboardButton(text="إيقاف ❌", callback_data="set_off")],
        [InlineKeyboardButton(text="🔙 العودة", callback_data="btn_home")]
    ])
    await call.message.edit_text(f"⚙️ {html.bold('إعدادات التذكير الدوري')}\n\nاختر الفترة الزمنية:", reply_markup=kb, parse_mode="HTML")

@dp.callback_query(F.data.startswith("set_"))
async def handle_save_settings(call: CallbackQuery):
    if not await is_admin(call): return
    val = call.data.split("_")[1]
    cid = call.message.chat.id
    if val == "off":
        active_chats.pop(cid, None)
        await call.answer("✅ تم الإيقاف", show_alert=True)
    else:
        active_chats[cid] = {"interval": float(val), "last": time.time()}
        await call.answer(f"✅ تم التفعيل كل {val} ساعة", show_alert=True)
    await back_home(call)

@dp.callback_query(F.data == "btn_home")
async def back_home(call: CallbackQuery):
    bot_info = await call.bot.get_me()
    await call.message.edit_text(text_welcome(), reply_markup=kb_main(bot_info.username), parse_mode="HTML")

@dp.callback_query(F.data == "btn_random")
async def btn_random_dhikr(call: CallbackQuery):
    dk = random.choice(ADHKAR_LIST)
    await call.message.edit_text(
        f"✨ {html.bold('الذكر اليومي:')}\n\n{html.code(dk)}", 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔄 ذكر آخر", callback_data="btn_random")],
            [InlineKeyboardButton(text="🔙 عودة", callback_data="btn_home")]
        ]),
        parse_mode="HTML"
    )

# --- [ نظام الترحيب البثي ] ---
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=F.NEW_STATUS.IN_({ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER})))
async def on_bot_join(event: ChatMemberUpdated):
    if event.new_chat_member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR]:
        welcome = (
            f"🎊 {html.bold('تم تفعيل نُورِفَاي في هذا المكان!')}\n\n"
            "سأقوم بنشر الأذكار والأدعية.\n"
            "💡 المشرفون يمكنهم تغيير أوقات التذكيرات من الضبط الدوري."
        )
        try:
            await event.bot.send_message(event.chat.id, welcome, parse_mode="HTML")
        except Exception:
            pass

async def background_broadcaster(bot: Bot):
    while True:
        now = time.time()
        for cid, config in list(active_chats.items()):
            if now - config["last"] >= (config["interval"] * 3600):
                try:
                    dhikr = random.choice(ADHKAR_LIST)
                    await bot.send_message(cid, f"💠 {html.bold('نفحات نُورِفَاي:')}\n\n{html.code(dhikr)}", parse_mode="HTML")
                    active_chats[cid]["last"] = now
                except Exception as e:
                    if "forbidden" in str(e).lower() or "not found" in str(e).lower():
                        active_chats.pop(cid, None)
        await asyncio.sleep(60)

# --- [ معالجات الـ Webhook المستقرة ] ---
async def handle_webhook(request: web.Request) -> web.Response:
    try:
        bot: Bot = request.app['bot']
        data = await request.json()
        update = Update(**data)
        await dp.feed_update(bot, update)
    except Exception as e:
        logging.error(f"خطأ أثناء معالجة التحديث: {e}")
    return web.Response(text="OK")

async def on_startup(bot: Bot):
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await asyncio.sleep(1)
        await bot.set_webhook(WEBHOOK_URL)
        print(f"✅ تم تعيين الـ Webhook الجديد بنجاح على: {WEBHOOK_URL}")
    except Exception as e:
        print(f"❌ خطأ في إعدادات الـ Webhook: {e}")

async def on_shutdown(bot: Bot):
    await bot.delete_webhook()
    print("🔌 تم إغلاق الاتصال البرمي")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.create_task(background_broadcaster(bot))
    await bot.set_my_commands([
        BotCommand(command="start", description="🌟 فتح القائمة الرئيسية"),
        BotCommand(command="help", description="🆘 المساعدة"),
        BotCommand(command="guide", description="📑 دليل الاستخدام"),
        BotCommand(command="stats", description="📊 الإحصائيات"),
    ])
    await on_startup(bot)
    app = web.Application()
    app['bot'] = bot
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"💎 NOORIFY BOT IS RUNNING ON PORT {PORT}")
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        await on_shutdown(bot)
        await runner.cleanup()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
