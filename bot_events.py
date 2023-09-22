from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import bot_ii

def init(router: Router):
    @router.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer("Здайте мне вопрос")

    @router.message()
    async def callback_how_its_works(message: Message) -> None:
        answer = bot_ii.get_answer(message.text)
        text = "Категория: " + answer['category'] + "\r\n\r\n" + answer['answer']
        await message.answer(text)