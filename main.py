import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from parser import parse_questions


logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 أهلاً بك في بوت الاختبارات.\n\n"
        "أرسل الأسئلة بهذه الطريقة:\n\n"
        "السؤال؟\n"
        "✓ الخيار الصحيح\n"
        "الخيار الثاني\n"
        "الخيار الثالث\n\n"
        "ضع سطرًا فارغًا بين كل سؤال."
    )


@dp.message()
async def create_quiz(message: Message):
    questions = parse_questions(message.text)

    if not questions:
        await message.answer(
            "❌ لم أجد أسئلة صحيحة.\n"
            "تأكد من وضع ✓ أمام الإجابة الصحيحة."
        )
        return

    for q in questions:
        await bot.send_poll(
            chat_id=message.chat.id,
            question=q["question"],
            options=q["options"],
            type="quiz",
            correct_option_id=q["correct"],
            is_anonymous=False
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
