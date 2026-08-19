import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS, REQ_CHANNEL1, REQ_CHANNEL2
from database.users_chats_db import db
from database.ia_filterdb import Media, Mediaa, db as clientDB, db1 as clientDB2, db2 as clientDB3
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

@Client.on_message(filters.command('check') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    tot = await Media.count_documents()
    tota = await Mediaa.count_documents()
    total = tot + tota
    users = await db.total_users_count()
    chats = await db.total_chat_count()
    stats = await clientDB.command('dbStats')
    used_dbSize = (stats['dataSize']/(1024*1024))+(stats['indexSize']/(1024*1024))        
    free_dbSize = 512-used_dbSize
    stats2 = await clientDB2.command('dbStats')
    used_dbSize2 = (stats2['dataSize']/(1024*1024))+(stats2['indexSize']/(1024*1024))
    free_dbSize2 = 512-used_dbSize2
    stats3 = await clientDB3.command('dbStats')
    used_dbSize3 = (stats3['dataSize']/(1024*1024))+(stats2['indexSize']/(1024*1024))
    free_dbSize3 = 512-used_dbSize3
    await rju.edit(script.STATUS_TXT2.format(total, tot, round(used_dbSize2, 2), round(free_dbSize2, 2), tota, round(used_dbSize3, 2), round(free_dbSize3, 2), users, chats, round(used_dbSize, 2), round(free_dbSize, 2)))

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    rju = await message.reply("`Processing... Please wait...`")
    chats = await db.get_all_chats()  
    file_name = "chats.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("List of Chats/Groups connected to the bot:\n\n")
        async for chat in chats:
            chat_id = chat.get('id', 'N/A')
            chat_title = chat.get('title', 'Unknown Title')
            file.write(f"Chat Title: {chat_title} | Chat ID: {chat_id}\n")
    if os.path.exists(file_name):
        with open(file_name, 'rb') as doc:
            await message.reply_document(doc, caption="List Of Chats")
        await rju.delete()
        os.remove(file_name)
    else:
        await rju.edit("Failed to generate chats.txt file!")



@Client.on_message(filters.command('purge_one') & filters.private & filters.user(ADMINS))
async def purge_req_one(bot, message):
    r = await message.reply("`processing...`")
    await db.delete_all_one()
    await r.edit("**Req db Cleared**" )


@Client.on_message(filters.command('purge_two') & filters.private & filters.user(ADMINS))
async def purge_req_two(bot, message):
    r = await message.reply("`processing...`")
    await db.delete_all_two()
    await r.edit("**Req db Cleared**" )

@Client.on_message(filters.command("totalreq") & filters.user(ADMINS))
async def total_requests(bot, message): 
    rju = await message.reply('Fetching stats..')
    total_one = await db.get_all_one_count()
    total_two = await db.get_all_two_count()
    if REQ_CHANNEL1 != False: 
        req_channel1 = await bot.get_chat(REQ_CHANNEL1)
        req_channel1 = req_channel1.title
    else:
        req_channel1 = "REQ_CHANNEL1"
    if REQ_CHANNEL2 != False:
        req_channel2 = await bot.get_chat(REQ_CHANNEL2)
        req_channel2 = req_channel2.title
    else:
        req_channel2 = "REQ_CHANNEL2"
    await rju.edit(f"{req_channel1} : {total_one}\n{req_channel2} : {total_two}")
