import os
import sys
import random
from datetime import datetime
from time import time
from time import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
import asyncio
from pyrogram import Client, filters
from config import HNDLR
from MusicTop.helpers.get_file_id import get_file_id
from MusicTop.helpers.merrors import capture_err
from MusicTop.helpers.decorators import authorized_users_only

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تحديث"], prefixes=f"{HNDLR}"))
@authorized_users_only

async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("•انتضر عزيزي \n سيتم تحديث سورس يرجا الانتضار قليلا")
    sleep(9)
    await loli.edit("**✅ تم تحديث سورس ميوزك توب @IIIT5")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["اوامري"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def help(client, m: Message):
    await m.delete()
    TOPAC = f"""
<b> هلاا عمري  {m.from_user.mention}!
ـ——————×—————————
● | لتشغيل صوتية في المكالمة أرسل ⇦ [ {HNDLR}تشغيل  + اسم الاغنيه ]
● | لتشغيل فيديو في المكالمة  ⇦ [ {HNDLR}تشغيل_فيديو  + اسم الاغنية ]
ـ———————×————————
● | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ {HNDLR}استئناف ] 
● | لأعاده تشغيل الاغنية ⇦  [ {HNDLR}ايقاف_الاستئناف ]
● | لأيقاف الاغنية  ⇦ [ {HNDLR}ايقاف ] 
ـ———————×————————
● | لتحميل صوتية أرسل ⇦ [ {HNDLR}تحميل + اسم الاغنية او الرابط ]
● | لتحميل فيديو  ⇦  [ {HNDLR}تحميل_فيديو + اسم الاغنية او الرابط ]
ـ———————×————————
● | لعرض الايدي ⇦ [ `{HNDLR}ايدي` , `{HNDLR}ا` ]
● | لأعاده تشغيل السورس أرسل ⇦  [ {HNDLR}تحديث` ]
ـ———————×————————
المطور 🇮🇶 : @IIIT5
"""
    r = random.randint(64, 94)
    await m.reply_photo(f"https://t.me/QWERTYU8I/{r}", caption=TOPAC)
@Client.on_message(filters.command(["ايدي","ا"], prefixes=f"{HNDLR}"))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>-› ايدي الدردشة </b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>-› هذا ايديك</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>-› ايدي العضو</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
@Client.on_message(filters.command(["git", "github"], prefixes=f"{HNDLR}"))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await m.reply_text("/git Username")
        return
    username = m.text.split(None, 1)[1]
    URL = "https://github.com/MUSIC-TELEGRAM1/MUSIC-TELEGRAM1"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await m.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)
@Client.on_message(filters.command(["فحص"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    topac1 = f"""
<b>👋  اهلا {m.from_user.mention}!
•> سورس شغال الان \n ارسل `{HNDLR}اوامري` \n لتعرف اوامر السورس \n المطور @iiit5
"""
    r = random.randint(1,2314)
    await Client.send_audio(message.chat.id, audio=(f"https://t.me/AC2AA/{r}"), caption=topac1)
@Client.on_message(filters.command(["ف"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!
•> سورس شغال الان \n ارسل `{HNDLR}اوامري` \n لتعرف اوامر السورس \n المطور @iiit5
"""
    
    await m.reply(REPO, disable_web_page_preview=True)
