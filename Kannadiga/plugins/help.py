from Kannadiga import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Kannadiga import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/743570cee67092f5d03b7.jpg"

ZAID_Help = "❤️💛 ΛႺՕ𝖱Λ 𝖱ՕΒՕΤ 𝖲РΛМ 💛❤️\n\n"
 
ZAID_Help += f"_ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅᴇᴀᴅʟʏ ʙᴏ_ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴀɢᴏʀᴀ ʙᴏᴛ__\n\n"

ZAID_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

ZAID_Help += f" `.ping` - to check ping\n `.alive` - To Check Bot Alive/Version (Only Main Userbot Will Reply)\n .`restart` - To Restart All Spam Bot \n `.addecho` - To Add Echo \n `.rmecho` - To Remove Echo \n `.addsudo` - To Add Sudo User Using Spam Bot \n\n"
 
ZAID_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

ZAID_Help += f" `.leave` - To Leave Public/Private Channel/Groups\n\n"
 
ZAID_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

ZAID_Help += f" `.raid` - To Raid\n `.replyraid` - To Active Reply Raid\n `.dreplyraid` - To Deactivate Reply Raid\n `.spam` - This Is Used For Normal Spam\n `.bigspam` - This Is Used For Big Spam\n `.uspam` - This Is Used For Unlimited Spam Unt You Restart The Bots!!\n `.delayspam` - This Is Used For Delay Spam\n\n"

ZAID_Help += f" .zaidspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂😈↧\n\n"

ZAID_Help += f"© @AGORA_ROBOTS\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=ZAID_Help,
                                  buttons=[
        [
        Button.url("❤️ ᴄʜᴀɴɴᴇʟ ❤️", "https://t.me/AGORA_ROBOTS")
        ] 
        ]
        )                                                         
