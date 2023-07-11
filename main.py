from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup
from translate import Translator

bot = Bot('5723569322:AAHb4xdvy3mXQrY8h8CgEs2ZXIA1NCVs5_U')
dp = Dispatcher(bot)


#aa

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/w_p')
b2 = KeyboardButton('/spiegel')
b3 = KeyboardButton('/polska')
b4 = KeyboardButton('/japan')
b5 = KeyboardButton('/italy')
b6 = KeyboardButton('/kz')
b7 = KeyboardButton('/france')
kb.add(b1, b2).add(b3, b4).add(b5,b6).add(b7)

@dp.message_handler(text = 'П')
async def menu(message: types.Message):
    await message.answer(text = 'что будем читать?', reply_markup = kb)


@dp.message_handler(commands = ['france'])
async def italy(message: types.Message):
    link = 'https://www.lefigaro.fr/'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    block_main = soup.find('div', class_='fig-main-col').find('div',class_= 'fig-main').find_all('section', class_= 'fig-ensemble')

    block_1_header = block_main[0].find('article').find('a').text
    block_1_text = block_main[0].find('article').find('p').text
    block_1_link = block_main[0].find('article').find('a').get('href')
    block_1_dop = block_main[0].find('ul').find_all('li')
    block_1_dop_1 = block_1_dop[0].find('a').find('h2').text
    block_1_dop_1_link = block_1_dop[0].find('a').get('href')
    block_1_dop_2 = block_1_dop[1].find('a').find('h2').text
    block_1_dop_2_link = block_1_dop[1].find('a').get('href')

    block_2_header = block_main[1].find('article').find('a').text
    block_2_text = block_main[1].find('article').find('p').text
    block_2_link = block_main[1].find('article').find('a').get('href')

    block_3_header = block_main[2].find('article').find('a').text
    block_3_text = block_main[2].find('article').find('p').text
    block_3_link = block_main[2].find('article').find('a').get('href')

    translator = Translator(from_lang='fr', to_lang='ru')
    transl_block_1_header = translator.translate(block_1_header)
    transl_block_1_text = translator.translate(block_1_text)
    transl_block_1_dop_1 = translator.translate(block_1_dop_1)
    transl_block_1_dop_2 = translator.translate(block_1_dop_2)
    transl_block_2_header = translator.translate(block_2_header)
    transl_block_2_text = translator.translate(block_2_text)
    transl_block_3_header = translator.translate(block_3_header)
    transl_block_3_text = translator.translate(block_3_text)

    await message.answer(text=f"{transl_block_1_header} \n {transl_block_1_text} \n {block_1_link} \n\n "
                              f"{transl_block_1_dop_1} \n {block_1_dop_1_link} \n\n {transl_block_1_dop_2} \n {block_1_dop_2_link} "
                              f"\n\n {transl_block_2_header} \n {transl_block_2_text} \n {block_2_link} "
                              f"\n\n {transl_block_3_header} \n {transl_block_3_text} \n {block_3_link}", reply_markup = kb)

#парсинг и перевод репаблика итальянской
@dp.message_handler(commands=['italy'])
async def wash_post(message: types.Message):
    link = 'https://www.repubblica.it/'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    blocks = soup.find_all('section', class_='block')

    block_header_0 = blocks[0].find('h1').text
    block_1 = blocks[0].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('div', class_='entry__content').find('h2').find('a').text
    block_1_link = blocks[0].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('figure').find('a').get('href')
    block_2 = blocks[1].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('div', class_='entry__content').find('h2').find('a').text
    block_2_link = blocks[1].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('figure').find('a').get('href')
    block_3 = blocks[2].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('div', class_='entry__content').find('h2').find('a').text
    block_3_link = blocks[2].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('figure').find('a').get('href')
    block_4 = blocks[3].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('div', class_='entry__content').find('h2').find('a').text
    block_4_link = blocks[3].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('figure').find('a').get('href')
    block_5 = blocks[4].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('div', class_='entry__content').find('h2').find('a').text
    block_5_link = blocks[4].find('div', class_='block__grid').find('div', class_='block__item').find('article')\
        .find('figure').find('a').get('href')

    translator = Translator(from_lang='it', to_lang='ru')
    transl_block_header = translator.translate(block_header_0)
    transl_block_1 = translator.translate(block_1)
    transl_block_2 = translator.translate(block_2)
    transl_block_3 = translator.translate(block_3)
    transl_block_4 = translator.translate(block_4)
    transl_block_5 = translator.translate(block_5)
    await message.answer(
        text=f"{transl_block_header} \n {transl_block_1} \n {block_1_link} \n\n {transl_block_2} \n {block_2_link} \n\n {transl_block_3} \n\n {block_3_link} \n\n {transl_block_4} \n {block_4_link} \n\n {transl_block_5} \n\n {block_5_link}",
        reply_markup=kb)

#парсинг и перевод вашингтон пост
@dp.message_handler(commands=['w_p'])
async def wash_post(message: types.Message):
    link = 'https://www.washingtonpost.com/'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    blocks = soup.find_all('div', class_='card-left card-text next-to-art no-bottom')
    mini_blocks = soup.find_all('div', class_='card relative')

    block_1 = soup.find('div', class_='card-left card-text next-to-art no-bottom').find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').text
    block_1_link = soup.find('div', class_='card-left card-text next-to-art no-bottom').find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').get('href')
    block_2 = blocks[1].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').find('span').text
    block_2_link = blocks[1].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').get('href')
    block_3 = blocks[2].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').find('span').text
    block_3_link = blocks[2].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').get('href')
    block_4 = blocks[3].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').find('span').text
    block_4_link = blocks[3].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').get('href')
    block_5 = blocks[4].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').find('span').text
    block_5_link = blocks[4].find('div',class_='headline relative gray-darkest pb-xs')\
        .find('h2').find('a').get('href')

    translator = Translator(from_lang='en', to_lang='ru')
    transl_block_1 = translator.translate(block_1)
    transl_block_2 = translator.translate(block_2)
    transl_block_3 = translator.translate(block_3)
    await message.answer(text = f"{transl_block_1} \n {block_1_link} \n\n {transl_block_2} \n {block_2_link} \n\n {transl_block_3} \n\n {block_3_link}", reply_markup=kb)

@dp.message_handler(commands='polska')
async def polska(message: types.Message):
    link  = 'https://www.gazeta.pl/0,0.html'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')

    block_all = soup.find('div', class_='zsectionTiles__box').find_all('a')

    print(block_all)

def main():
    menu()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
