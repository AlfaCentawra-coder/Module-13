from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Напишите слово 'Калории' чтобы узнать необходимое количество каллорий в день")


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    activity = State()

@dp.message_handler(text = 'Калории')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserStates.age.set()

@dp.message_handler(state = UserStates.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост')
    await UserStates.growth.set()

@dp.message_handler(state = UserStates.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес')
    await UserStates.weight.set()

@dp.message_handler(state = UserStates.weight)
async def set_activity(message, state):
    await state.update_data(weight = message.text)
    await message.answer('Выберите свою активность \n'
                         'Минимальная активность 1.2 \n'
                         'Слабая активность 1.375 \n'
                         'Средняя активность 1.55 \n'
                         'Высокая активность 1.725 \n'
                         'Экстрa-активность 1.9')
    await UserStates.activity.set()

@dp.message_handler(state = UserStates.activity)
async def send_calories(message, state):
    await state.update_data(activity = message.text)
    data = await state.get_data()
    calories = (10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161) * float(data["activity"])
    await message.answer(f'Необходимое количество каллорий в день для вас {calories}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)