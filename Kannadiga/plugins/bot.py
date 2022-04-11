import os
import asyncio
import sys
import git
import heroku3
# Changed root to Kannadiga
from Kannadiga import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from Kannadiga import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, kannadigaversion
from Kannadiga import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from Kannadiga import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

KANNADIGA_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/fcf7fb7bcb39609e3f9fd.jpg"
  

DEADLY = "⚡ 𝗞𝗔𝗥𝗨𝗡𝗔𝗗𝗔 𝗙𝗜𝗚𝗛𝗧𝗘𝗥𝗦 ⚡\n\n"
DEADLY += f" ❤️𝐊𝐀𝐑𝐍𝐀𝐓𝐀𝐊𝐀's 𝟭𝐒𝐓 𝐁𝐎𝐓𝐒𝐏𝐀𝐌❤️\n\n"
DEADLY += f"╔═══════════════════════╗\n"
DEADLY += f"║• **ᴄʀᴇᴀᴛᴏʀ** :`ᴘʀᴏғᴇssᴏʀ ᴀɢᴏʀᴀ   `             ║\n"
DEADLY += f"║• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`               ║\n"
DEADLY += f"║• **ᴋᴀɴɴᴀᴅɪɢᴀ ʙᴏᴛ sᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{kannadigaversion}` ║\n"
DEADLY += f"╚═══════════════════════╝\n\n"   

                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await BOT0.send_file(event.chat_id,
                                  KANNADIGA_PIC,
                                  caption=DEADLY,
                                  buttons=[
        [
        Button.url("❤️ ᴄʜᴀɴɴᴇʟ ❤️", "https://t.me/KARUNADA_KINGS_AND_QUEENS"),
        Button.url("💛 sᴜᴘᴘᴏʀᴛ 💛", "https://t.me/KARUNADA_FIGHTERS")
        ],
        [
        Button.url("✨ ʀᴇᴘᴏ ✨", "https://github.com/MR-KANNADIGA/ROBOTSPAM")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🎉 𝗬𝗘𝗦 𝗕𝗢𝗦𝗦!\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎")
        
        

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Rebooting ↪️**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await BOT0.disconnect()
        except Exception:
            pass
        try:
            await BOT1.disconnect()
        except Exception:
            pass
        try:
            await BOT2.disconnect()
        except Exception:
            pass
        try:
            await BOT3.disconnect()
        except Exception:
            pass
        try:
            await BOT4.disconnect()
        except Exception:
            pass
        try:
            await BOT5.disconnect()
        except Exception:
            pass
        try:
            await BOT6.disconnect()
        except Exception:
            pass
        try:
            await BOT7.disconnect()
        except Exception:
            pass
        try:
            await BOT8.disconnect()
        except Exception:
            pass
        try:
            await BOT9.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding User As A Sudo...")
        DEADLY = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To A User.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** As A Sudo User 💛 Restarting.. Please wait a minute...")
        heroku_var[DEADLY] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
