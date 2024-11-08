import requests
from bs4 import BeautifulSoup
import keyboards as kb
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters.callback_data import CallbackData


cookies = {
    '__ddg1_': 'g9kcUf8Dus2yGtgo5X6j',
    '__ddg9_': '95.221.28.228',
    '__ddg8_': 'cbY5NCtfDZ5iZI7v',
    '__ddg10_': '1730161212',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=g9kcUf8Dus2yGtgo5X6j; __ddg9_=95.221.28.228; __ddg8_=cbY5NCtfDZ5iZI7v; __ddg10_=1730161212',
    'if-modified-since': 'Mon, 28 Oct 2024 09:57:24 GMT',
    'if-none-match': '"387f7-625867edd1e60-gzip"',
    'priority': 'u=0, i',
    'referer': 'https://zf-ranepa-rasp.ru/nov',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}


ssilkinovem = ['https://zf-ranepa-rasp.ru/nov04-nov09',
               'https://zf-ranepa-rasp.ru/nov11-nov16',
               'https://zf-ranepa-rasp.ru/nov18-nov23',
               'https://zf-ranepa-rasp.ru/nov25-nov30',]

ssilkidecem = ['https://zf-ranepa-rasp.ru/des02-des07',
               'https://zf-ranepa-rasp.ru/des09-des14',
               'https://zf-ranepa-rasp.ru/des16-des21',
               'https://zf-ranepa-rasp.ru/des23-des28']

id_div_nov = [['rec790239398','rec790239401','rec790239404','rec790239407','rec790239410','rec790239413'],
              ['rec790239428','rec790239431','rec790239434','rec790239437','rec790239440','rec790239443'],
              ['rec790240348','rec790240351','rec790240354','rec790240357','rec790240360','rec790240363'],
              ['rec790240377','rec790240380','rec790240383','rec790240386','rec790240389','rec790240392']]

id_div_dec = [['rec790249943','rec790249946','rec790249949','rec790249952','rec790249956','rec790249959'],
              ['rec790249965','rec790249968','rec790249971','rec790249974','rec790249977','rec790249980'],
              ['rec790251176','rec790251179','rec790251182','rec790251185','rec790251188','rec790251191'],
              ['rec790251222','rec790251225','rec790251228','rec790251231','rec790251234','rec790251237']]



bot = Bot(token='8167261602:AAEladK25_KvB_ZEy9504GBSXYKO8vG9OwA')
dp = Dispatcher()

class GoodsCallbackFactory\
        (CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int

class Search(StatesGroup):
    fam = State()
    month = State()
    group = State()


async def main():
    await dp.start_polling(bot)

#Выбор студент или препод
@dp.message(Command('start'))
async def start1(message: Message):
    await message.answer(f'Вас приветствует бот расписания РАНХиГС🦾')
    await message.answer('Вы студент или преподаватель?',reply_markup=kb.settings)


#После выбора кнопки студент или препод
@dp.callback_query(F.data == 'Студент')  #студент
async def stud(callback: CallbackQuery,state: FSMContext):
    await state.set_state(Search.group)
    await callback.answer('')
    await callback.message.answer(f'Привет, {callback.from_user.first_name}! Жду твоей команды⬇️', reply_markup=kb.main1)

@dp.message(F.text == '📚Расписание на неделю')
async def weakraspprep(message: Message,state: FSMContext):
    await state.set_state(Search.group)
    await message.answer('📈Введите Вашу группу:')


@dp.message(Search.group)
async def start2(message: Message, state:FSMContext):
    await state.update_data(group=message.text)
    await state.set_state(Search.month)
    await message.answer('📆Выберите месяц',reply_markup=kb.month2)

@dp.callback_query(F.data == 'Ноябрь1')
async def stud(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('📆Выберите неделю', reply_markup=kb.markup2)

@dp.callback_query(F.data == 'Декабрь1')
async def stud(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('📆Выберите неделю', reply_markup=kb.markup4)

@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 3))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory,state: FSMContext):
    response = requests.get(ssilkinovem[callback_data.item_id], cookies=cookies, headers=headers).text

    data = await state.get_data()
    for i in range(6):
        dni = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
        data1 = importtext(id_div_nov[callback_data.item_id][i], response)
        indic = indices(data1, data['group'])
        await callback.message.answer(dni[i], reply_markup=await kb.raspinline(indic, data1))
    await callback.answer()

@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 4))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory,state: FSMContext):
    response = requests.get(ssilkidecem[callback_data.item_id], cookies=cookies, headers=headers).text

    data = await state.get_data()
    for i in range(6):
        dni = ['🎓Понедельник','💻Вторник','📚Среда','👨🏻‍🎓Четверг','👩🏼‍🎓Пятница','💃🏻Суббота']
        data1 = importtext(id_div_dec[callback_data.item_id][i], response)
        indic = indices(data1, data['group'])
        await callback.message.answer(dni[i], reply_markup=await kb.raspinline(indic, data1))
    await callback.answer()








@dp.callback_query(F.data == 'Преподаватель') #препод
async def prepod(callback: CallbackQuery,state: FSMContext):
    await callback.answer('')
    await callback.message.answer(f'Здравствуйте, {callback.from_user.first_name}! Жду вашей команды⬇️', reply_markup=kb.main2)


@dp.message(F.text == '📚Недельное расписание')
async def weakraspprep(message: Message,state: FSMContext):
    await state.set_state(Search.fam)
    await message.answer('📈Введите Вашу фамилию:')


@dp.message(Search.fam)
async def start2(message: Message, state:FSMContext):
    await state.update_data(fam=message.text)
    await state.set_state(Search.month)
    await message.answer('📆Выберите месяц',reply_markup=kb.month1)

@dp.callback_query(F.data == 'Ноябрь')
async def stud(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('📆Выберите неделю', reply_markup=kb.markup)

@dp.callback_query(F.data == 'Декабрь')
async def stud(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('📆Выберите неделю', reply_markup=kb.markup1)




@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 1))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory,state: FSMContext):
    response = requests.get(ssilkinovem[callback_data.item_id], cookies=cookies, headers=headers).text

    data = await state.get_data()
    for i in range(6):
        dni = ['🎓Понедельник','💻Вторник','📚Среда','👨🏻‍🎓Четверг','👩🏼‍🎓Пятница','💃🏻Суббота']
        data1 = importtext(id_div_nov[callback_data.item_id][i], response)
        indic = indices(data1, data['fam'])
        await callback.message.answer(dni[i], reply_markup=await kb.raspinline1(indic, data1))
    await callback.answer()

@dp.callback_query(GoodsCallbackFactory.filter(F.category_id == 2))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory,state: FSMContext):
    response = requests.get(ssilkidecem[callback_data.item_id], cookies=cookies, headers=headers).text

    data = await state.get_data()
    for i in range(6):
        dni = ['🎓Понедельник','💻Вторник','📚Среда','👨🏻‍🎓Четверг','👩🏼‍🎓Пятница','💃🏻Суббота']
        data1 = importtext(id_div_dec[callback_data.item_id][i], response)
        indic = indices(data1, data['fam'])
        await callback.message.answer(dni[i], reply_markup=await kb.raspinline1(indic, data1))
    await callback.answer()

def indices(data,search_string): #вывод информации для группы на день
    indices = []
    for index, value in enumerate(data):
        if search_string in value:
            indices.append(index)
    if indices == []:
        return []
    return indices

def importtext(id1,ssilka): #ДЕЛАЕМ ЧИСТЫЙ ТЕКСТ
    soup = BeautifulSoup(ssilka, 'lxml')
    block = soup.find('div', id=id1)
    info_block = block.find("div", {"class": "t431__data-part2"})
    a = info_block.get_text().replace('\n', '').split(';')
    return a


















if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')