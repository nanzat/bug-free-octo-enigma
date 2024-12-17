import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from transliterate import translit
from transliterate.discover import autodiscover
from transliterate.base import TranslitLanguagePack, registry


autodiscover()

class NewRuss(TranslitLanguagePack):
    language_code = "ru2020"
    language_name = "Russian2020"
    mapping = (
       u"АБВГДЕЁЗИЙКЛМНОПРСТУФЫЭЬ",
       u"ABVGDEEZIIKLMNOPRSTUFYE'",
    )
    pre_processor_mapping = {
        u'Ж': u'ZH',
        u'Х': u'KH',
        u'Ц': u'TS',
        u'Ч': u'CH',
        u'Ш': u'SH',
        u'Щ': u'SHCH',
        u'Ъ': u'IE',
        u'Ю': u'IU',
        u'Я': u'IA',
    }
registry.register(NewRuss)

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename = "logs.log")


@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello {user_name}'
    logging.info(f'{user_name} {user_id} has started bot')
    await bot.send_message(chat_id=user_id, text=text)
    await bot.send_message(chat_id=user_id, text='Please send your full name')

@dp.message()
async def process_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name} {user_id} message:{message.text}')

    text = message.text
    response = list()
    for i in text.upper().split():
        if not i.isalpha():
            await message.answer(text='Full name must follow the format:\nSurname Forename Patronymic')
            logging.info(f'{user_name} {user_id} wrong format')
            break
        response.append(translit(i, language_code='ru2020'))
    logging.info(f'{user_name} {user_id} success')
    await message.answer(text=' '.join(response))


if __name__ == '__main__':
    dp.run_polling(bot)


