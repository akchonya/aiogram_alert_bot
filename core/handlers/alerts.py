import asyncio
import datetime

from os import getenv
from dotenv import load_dotenv
from alerts_in_ua import AsyncClient as AsyncAlertsClient
from aiogram import types, Router
from aiogram.filters import Command
from aiogram import Bot

load_dotenv()
ALERTS_TOKEN = getenv("ALERTS_TOKEN")
DORM_CHAT_ID = getenv("DORM_CHAT_ID")

alerts_router = Router()

@alerts_router.message(Command("alerts"))
async def alerts_handler(message: types.Message, bot: Bot):
    lviv_status = "start"
    msg = None
    while True:
        alerts_client = AsyncAlertsClient(token=ALERTS_TOKEN)
        active_alerts = await alerts_client.get_air_raid_alert_statuses_by_oblast()
        lviv = str([alert for alert in active_alerts if alert.location_title == "Львівська область"][0])[:-17]
        print(f"[{datetime.datetime.now()}] {lviv}")
        if lviv_status != lviv:
            lviv_status = lviv
            await message.answer(f"Alert update: {lviv}",
                                 reply_markup=types.ReplyKeyboardRemove())
            if lviv == "active":
                msg = await bot.send_video(DORM_CHAT_ID, 
                                video="BAACAgIAAxkBAAEmB3JlBgLAVXsNL-BTjEMPE6Pk4YBN_AACNx4AAmqumUr1ey8JH10sPDAE")
                await bot.send_message(DORM_CHAT_ID, "🚨 <b>ТРИВОГА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</b>\n" +
                                    "ПАКУЙТЕ СМАКОЛИКИ І У СХОВИЩЕ \n\n" +
                                    "<tg-spoiler>або під ковдру на свій страх і ризик</tg-spoiler>", 
                                    parse_mode="HTML")
                await bot.pin_chat_message(DORM_CHAT_ID, msg.message_id, True)
            else:
                if msg != None:
                    await bot.send_message(DORM_CHAT_ID, "✅ ВІДБІЙ ТРИВОГИ")
                    await bot.unpin_chat_message(DORM_CHAT_ID, msg.message_id)
            
        await asyncio.sleep(60)
