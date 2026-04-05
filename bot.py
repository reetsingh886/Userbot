import os
import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, UserDeactivatedBan, UserBannedInChannel
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")
control_group = int(os.getenv("CONTROL_GROUP_ID"))

app = Client(session_string=session_string, api_id=api_id, api_hash=api_hash)

auto_send = False
custom_message = "👋 Hello group!"
interval = 10  # default in minutes

async def auto_sender():
    global auto_send
    while auto_send:
        async for dialog in app.get_dialogs():
            if dialog.chat.type in ["group", "supergroup"]:
                try:
                    await app.send_message(dialog.chat.id, custom_message)
                    await asyncio.sleep(2)
                except Exception as e:
                    # Notification for ban/mute in group
                    error_text = str(e).lower()
                    if "banned" in error_text or "not enough rights" in error_text or "muted" in error_text:
                        await app.send_message(control_group, f"⚠️ Can't send in {dialog.chat.title} (`{dialog.chat.id}`):\n`{e}`")
        await asyncio.sleep(interval * 60)

@app.on_message(filters.chat(control_group) & filters.command("startauto"))
async def start_auto(client, message):
    global auto_send
    if not auto_send:
        auto_send = True
        asyncio.create_task(auto_sender())
        await message.reply("✅ Auto messaging started.")
        await client.send_message(control_group, "🚀 Auto message sending **started**.")
    else:
        await message.reply("⚠️ Already running.")

@app.on_message(filters.chat(control_group) & filters.command("stopauto"))
async def stop_auto(client, message):
    global auto_send
    auto_send = False
    await message.reply("🛑 Auto messaging stopped.")
    await client.send_message(control_group, "⛔ Auto message sending **stopped**.")

@app.on_message(filters.chat(control_group) & filters.command("setmsg"))
async def set_msg(client, message):
    global custom_message
    if len(message.command) < 2:
        return await message.reply("⚠️ Use like: `/setmsg Your Message`")
    custom_message = message.text.split(" ", 1)[1]
    await message.reply("✏️ Message updated.")
    await client.send_message(control_group, f"📝 New message set:\n\n{custom_message}")

@app.on_message(filters.chat(control_group) & filters.command("setinterval"))
async def set_interval(client, message):
    global interval
    if len(message.command) < 2 or not message.command[1].isdigit():
        return await message.reply("⚠️ Use like: `/setinterval 10`")
    interval = int(message.command[1])
    await message.reply(f"⏱ Interval set to {interval} minutes.")
    await client.send_message(control_group, f"🔁 Auto message interval set to **{interval} minutes**.")

app.run()
