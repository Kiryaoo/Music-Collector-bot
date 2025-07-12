import logging
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import F
import yt_dlp

load_dotenv()
bot = Bot(
    token=os.getenv("BOT_TOKEN"), 
    default=DefaultBotProperties(parse_mode=None)
)
dp = Dispatcher()

class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer('Hi! Send me a song name using /sea <query>')

@dp.message(Command("sea"))
async def search_cmd(message: Message):
    arg = message.text.replace("/sea", "").strip()

    YDL_OPTIONS = {
        'format': 'bestaudio/best',
                   'noplalist': 'True',
                   'postprocessor':[{
                     'key':'FFmpegExtractAudio',
                     'preferredquality': '192'
        }]
    }

    filename_collector = FilenameCollectorPP()
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.add_post_processor(filename_collector)

        try:
            video = ydl.extract_info(f"ytsearch:{arg}", download=True)['entries'][0]
        except Exception as e:
            await message.answer(f"Error: {str(e)}")
            return

    if filename_collector.filenames:
        file_path = filename_collector.filenames[0]
        await message.answer_document(FSInputFile(file_path))
        await asyncio.sleep(5)
        os.remove(file_path)
    else:
        await message.answer("File not found or download failed.")
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())