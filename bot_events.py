import os
import speech_recognition as sr
from pydub import AudioSegment

from pathlib import Path
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Router

import bot_ii

def init(bot: Bot, router: Router):
    recognizer = sr.Recognizer()

    @router.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer("Здайте мне вопрос")

    @router.message(F.voice)
    async def voice_message_handler(message: Message):
        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        
        file_on_disk = Path("", f"{file_id}.tmp")
        await bot.download_file(file_path, destination=file_on_disk)

        AudioSegment.from_ogg(str(file_on_disk)).export(Path("", f"{file_id}.wav"), format="wav")
        os.remove(file_on_disk)  # Удаление временного файла

        file_on_disk = Path("", f"{file_id}.wav")

        # Загружаем аудио файл
        audio_file = sr.AudioFile(str(file_on_disk))
        
        # Распознаем речь из аудио файла
        with audio_file as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language = 'ru')
        
        # Выводим текст
        print(text)
        os.remove(file_on_disk)  # Удаление временного файла

        answer = bot_ii.get_answer(text)
        text = "Категория: " + answer['category'] + "\r\n\r\n" + answer['answer']
        await message.answer(text)

    @router.message()
    async def callback_how_its_works(message: Message) -> None:
        answer = bot_ii.get_answer(message.text)
        text = "Категория: " + answer['category'] + "\r\n\r\n" + answer['answer']
        await message.answer(text)