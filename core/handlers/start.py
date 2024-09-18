"""
/start greets a user
/help sends a list of aavailable commands
"""

from aiogram import F, Bot, types, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove
from datetime import datetime, timedelta
from ..utils.config import ADMIN_IDS


router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"<b>привіт, {html.unparse(message.from_user.first_name)} 😎</b>\n"
        + "я - ботік помічник для третього гурту лну.\n"
        + "можеш подивитися усі доступні команди в меню.\n\n"
        + f"якщо маєш питання чи пропозиції - <a href='tg://user?id={ADMIN_IDS[0]}'>звертайся</a>",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(
        f"<b>привіт, {message.from_user.first_name}!</b>\n\n"
        + "<b>ось список доступних команд:</b>\n"
        + "• /faq присилає корисну статтю\n"
        + "• /vahta - графік вахтерів\n"
        + "• /bunt i /rusoriz кидають відповідні стікери\n"
        + "• /weather_now i /weather_today показують погоду зараз і на сьогодні відповідно\n"
        + "• за допомогою /donate можеш підтримати розробницю бота\n\n"
        + f"якщо маєш питання чи пропозиції - <a href='tg://user?id={ADMIN_IDS[0]}'>звертайся</a>",
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),
    )


empty_router = Router()


@empty_router.message(F.dice.emoji == "🎰", F.dice.value != 64)
async def dice(message: types.Message, bot: Bot):
    # Get the current datetime
    now = datetime.now()

    # Calculate today's 10 AM
    today_10am = now.replace(hour=10, minute=0, second=0, microsecond=0)

    # Determine whether to use today's or next day's 10 AM
    if now > today_10am:
        # If the current time is after 10 AM, set to next day's 10 AM
        next_day = now + timedelta(days=1)
        result = next_day.replace(hour=10, minute=0, second=0, microsecond=0)
    else:
        # If the current time is before or exactly 10 AM, set to today's 10 AM
        result = today_10am

    await bot.restrict_chat_member(
        message.chat.id,
        message.from_user.id,
        types.ChatPermissions(False),
        until_date=result,
    )


@empty_router.message()
async def empty():
    pass
