"""
    answers "ні", "Ні", "нІ", "НІ"
"""


from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from core.utils.config import INTRO_ID
from core.utils.soup import parse_page

router = Router()


@router.message(F.text == "ні")
async def hi_lower_handler(message: Message):
    await message.reply("неllo", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "НІ")
async def hi_upper_handler(message: Message):
    await message.reply("НЕLLO", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "Ні")
async def hi_cap_handler(message: Message):
    await message.reply("Нello", reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "нІ")
async def hi_crazy_handler(message: Message):
    await message.reply("нEllO", reply_markup=ReplyKeyboardRemove())


intro_hi = ["Нї", "нї", "нЇ", "НЇ"]
intro_hello = ["Heїїo", "неїїо", "неЇЇо", "НЕЇЇО"]


@router.message((F.text.in_(intro_hi)) & (F.from_user.id == INTRO_ID))
async def hi_intro_handler(message: Message):
    await message.reply(intro_hello[intro_hi.index(message.text)])


@router.message(Command("svyato"))
async def svyaro_handler(message: Message):
    svyato = await parse_page("https://daytoday.ua/sogodni/")
    await message.answer(
        f"🍾 <b>свята сьогодні:</b>\n{svyato}", reply_markup=ReplyKeyboardRemove()
    )
