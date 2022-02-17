#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import JPG0 as file
from LOCAL.localisation import JPG4
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'𝐇𝐞𝐲 [{event.sender.first_name}](tg://user?id={event.sender_id})\n\n𝐈'𝐦 𝐚 𝐕𝐢𝐝𝐞𝐨 𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐨𝐫 𝐁𝐨𝐭 𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐀𝐧𝐲 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐕𝐢𝐝𝐞𝐨𝐬 𝐈'𝐥𝐥 𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬 𝐢𝐭 𝐅𝐨𝐫 𝐘𝐨𝐮. \n𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @ChVivekTomar', 
                      buttons=[[
                         Button.inline("🌌 SET THUMB", data="sett"),
                         Button.inline("🗑️ DEL THUMB", data='remt')],
                         [
                         Button.inline("❔ HELP", data="plugins"),
                         Button.inline("🗜️ RESTART", data="restart")],
                         [
                         Button.inline("🎇 NOTICE", data="notice")],
                         [
                         Button.url("👲 DEV", url=f"t.me/ChVivekTomar")]])

    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    

    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    

    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[Button.inline("NOTICE", data="notice")]])
                   
 #-----------------------------------------------------------------------------------------------                            
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("𝐒𝐞𝐧𝐝 𝐦𝐞 𝐀𝐧𝐲 𝐈𝐦𝐚𝐠𝐞 𝐟𝐨𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐚𝐬 𝐚 '𝐑𝐞𝐩𝐥𝐲' 𝐭𝐨 𝐓𝐡𝐢𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("𝐍𝐨 𝐦𝐞𝐝𝐢𝐚 𝐟𝐨𝐮𝐧𝐝.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("𝐍𝐨 𝐢𝐦𝐚𝐠𝐞 𝐟𝐨𝐮𝐧𝐝.")
        await set_thumbnail(event, x.media)
        await xx.delete()
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.delete()
    await rem_thumbnail(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("𝐎𝐧𝐥𝐲 𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫 𝐜𝐚𝐧 𝐑𝐞𝐬𝐭𝐚𝐫𝐭!")
    result = await heroku_restart()
    if result is None:
        await event.edit("𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐧𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝 `𝐇𝐄𝐑𝐎𝐊𝐔_𝐀𝐏𝐈` 𝐚𝐧𝐝 `𝐇𝐄𝐑𝐎𝐊𝐔_𝐀𝐏𝐏_𝐍𝐀𝐌𝐄` 𝐕𝐚𝐫𝐬.")
    elif result is False:
        await event.edit("𝐀𝐧 𝐄𝐫𝐫𝐨𝐫 𝐎𝐜𝐜𝐮𝐫𝐞𝐝!")
    elif result is True:
        await event.edit("𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐀𝐩𝐩 😉, 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐚 𝐌𝐢𝐧𝐮𝐭𝐞.")
