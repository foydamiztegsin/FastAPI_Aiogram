from aiogram import Dispatcher,Bot,types

TOKEN = "BOT TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Assalomu alaykum!")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
