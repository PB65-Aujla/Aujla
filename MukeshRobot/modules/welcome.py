import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MukeshRobot import app  

photo = [
    "https://telegra.ph/file/3a8e20cb22b8019f7f8ef.mp4",
    "https://telegra.ph/file/72f73d4bf50d09ca60e31.mp4",
    "https://telegra.ph/file/6f79d5c44e73b561dd0ea.mp4",
    "https://telegra.ph/file/b921678b35a7c59a4da42.mp4",
    "https://telegra.ph/file/05d248a4814930ad62b33.mp4",
    "https://telegra.ph/file/1a8a05e0d2277831eea9e.mp4",
    "https://telegra.ph/file/4555df5a4c85b55f8d32f.mp4",
    "https://telegra.ph/file/dd6519bfa31b43a640b1e.mp4",
    "https://telegra.ph/file/83234f8624b711911240d.mp4",
    "https://telegra.ph/file/a05db7b01d8746ee2d1d2.mp4",
    "https://telegra.ph/file/9b9b17475a523d1bf76c6.mp4",
    "https://telegra.ph/file/844d75d4811dfa36a31d6.mp4",
    "https://telegra.ph/file/ce22353d9cb92fa48e06b.mp4",
    "https://telegra.ph/file/c0279137fc6e8446ad948.mp4",
    "https://telegra.ph/file/9e32e5f5c5446bb599602.mp4",
    "https://telegra.ph/file/5cc70b3527164ef776c2c.mp4",
    "https://telegra.ph/file/08cb3212ff494e5d609c7.mp4",
    "https://telegra.ph/file/1f6423cf9d11757b73e92.mp4",
    "https://telegra.ph/file/de88aba93e783ddaf34f5.mp4",
    "https://telegra.ph/file/92905eb7dde15adc7f59d.mp4",
    "https://telegra.ph/file/a3399161732850f7f31c2.mp4",
    "https://telegra.ph/file/6c8cd92639b37705d4b5e.mp4",
    "https://telegra.ph/file/13aed4985f6261d83f997.mp4",
    "https://telegra.ph/file/696d29fa185fc9345fd60.mp4",
    "https://telegra.ph/file/865646133f15c3f7879b1.mp4",
    "https://telegra.ph/file/42afb550f38ea509d5cf4.mp4",
    "https://telegra.ph/file/6988f78934bddc650e2f8.mp4",
    "https://telegra.ph/file/4d8dd7b8a28f05210a7d6.mp4",
    "https://telegra.ph/file/645245962a6cce628235d.mp4",
    "https://telegra.ph/file/30f0775cf0e21c304b4ff.mp4",
    "https://telegra.ph/file/c601690e919722a0bc328.mp4",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
