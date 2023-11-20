from aiogram import Router, F
from aiogram.types import ReplyKeyboardRemove, Message

router = Router()


@router.message(F.text.contains("ні"))
async def hi_lower_handler(message: Message):
    await message.reply("неllo", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.contains("НІ"))
async def hi_upper_handler(message: Message):
    await message.reply("НЕLLO", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.contains("Ні"))
async def hi_cap_handler(message: Message):
    await message.reply("Нello", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.contains("нІ"))
async def hi_crazy_handler(message: Message):
    await message.reply("нEllO", reply_markup=ReplyKeyboardRemove())