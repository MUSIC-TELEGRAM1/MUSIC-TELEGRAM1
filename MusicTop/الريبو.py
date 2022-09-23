import os
import sys
from datetime import datetime
from time import time
from time import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
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


——————×—————

● | لتشغيل صوتية في المكالمة أرسل ⇦ [ {HNDLR}تشغيل  + اسم الاغنيه ]
● | لتشغيل فيديو في المكالمة  ⇦ [ {HNDLR}تشغيل_فيديو  + اسم الاغنية ]
———————×———————

● | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ {HNDLR}استئناف ] 
● | لأعاده تشغيل الاغنية ⇦  [ {HNDLR}ايقاف_الاستئناف ]
● | لأيقاف الاغنية  ⇦ [ {HNDLR}ايقاف ] 
———————×———————

● | لتحميل صوتية أرسل ⇦ [ {HNDLR}تحميل + اسم الاغنية او الرابط ]
● | لتحميل فيديو  ⇦  [ {HNDLR}تحميل_فيديو + اسم الاغنية او الرابط ]
———————×———————

● | لأعاده تشغيل السورس أرسل ⇦  [ {HNDLR}تحديث` ]
———————×———————
المطور 🇮🇶 : @IIIT5
"""
    await m.reply_photo("https://telegra.ph/file/8dd7aa6ad40d9262c89d1.jpg", caption=TOPAC)
@Client.on_message(filters.command(["فحص"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!
•> سورس شغال الان \n ارسل `{HNDLR}اوامري` \n لتعرف اوامر السورس \n المطور @iiit5
"""
    await m.reply(REPO, disable_web_page_preview=True)
