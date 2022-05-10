import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from Kannadiga import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

KANNADIGA_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/743570cee67092f5d03b7.jpg"

Deadly_Button = [
        [
        Button.url("❤️ sᴜᴘᴘᴏʀᴛ ❤️", "https://t.me/AGORA_ROBOTS")
        ],
        [
        Button.url("💛 ΛႺՕ𝖱Λ 💛", "https://t.me/MR_AGORA")
        ]
        ]
               
DeadlyX_Button = [
        [
        Button.url("❤️ ᴄʜᴀɴɴᴇʟ ❤️", "https://t.me/AGORA_ROBOTS"),
        Button.url("💛 sᴜᴘᴘᴏʀᴛ 💛", "https://t.me/KARUNADA_KINGS_AND_QUEENS")
        ],
        [
        Button.url("✨ ʀᴇᴘᴏ ✨", "https://github.com/MR-KANNADIGA/ROBOTSPAM")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DeadlyBot = await event.client.get_me()
       bot_id = DeadlyBot.first_name
       bot_username = DeadlyBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDeadly = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its Me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDeadly,
                  KANNADIGA_IMG,
                  caption=ownermsg, 
                  buttons=Deadly_Button)
       else:
            await event.client.send_file(TheDeadly,
                  KANNADIGA_IMG,
                  caption=usermsg, 
                  buttons=DeadlyX_Button)
                
