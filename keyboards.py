from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
main1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '📚Расписание на неделю')]
],          resize_keyboard=True,
            input_field_placeholder='Выберите расписание')
main2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = '📚Недельное расписание')],

],          resize_keyboard=True,
            input_field_placeholder='Выберите расписание')



settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👨🏻‍🎓Студент👩🏼‍🎓', callback_data='Студент')],
    [InlineKeyboardButton(text='👨🏼‍🏫Преподаватель👩🏼‍🏫', callback_data='Преподаватель')]])

month1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🍁Ноябрь', callback_data='Ноябрь')],
    [InlineKeyboardButton(text='❄️Декабрь', callback_data='Декабрь')]])

month2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🍁Ноябрь', callback_data='Ноябрь1')],
    [InlineKeyboardButton(text='❄️Декабрь', callback_data='Декабрь1')]])

class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int

button_1 = InlineKeyboardButton(
    text='📆04-09 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    ).pack()
)


button_2 = InlineKeyboardButton(
    text='📆11-16 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=1
    ).pack()
)
button_3 = InlineKeyboardButton(
    text='📆18-23 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=2
    ).pack()
)
button_4 = InlineKeyboardButton(
    text='📆25-30 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=3
    ).pack()
)
markup = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],[button_2],[button_3],[button_4]],resize_keyboard=True
)
button_11 = InlineKeyboardButton(
    text='📆04-09 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=3,
        subcategory_id=0,
        item_id=0
    ).pack()
)


button_22 = InlineKeyboardButton(
    text='📆11-16 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=3,
        subcategory_id=0,
        item_id=1
    ).pack()
)
button_33 = InlineKeyboardButton(
    text='📆18-23 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=3,
        subcategory_id=0,
        item_id=2
    ).pack()
)
button_44 = InlineKeyboardButton(
    text='📆25-30 ноября',
    callback_data=GoodsCallbackFactory(
        category_id=3,
        subcategory_id=0,
        item_id=3
    ).pack()
)
markup2 = InlineKeyboardMarkup(
    inline_keyboard=[[button_11],[button_22],[button_33],[button_44]]
)
class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int

button1 = InlineKeyboardButton(
    text='📆02-07 декабряя',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    ).pack()
)


button2 = InlineKeyboardButton(
    text='📆09-14 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=1
    ).pack()
)
button3 = InlineKeyboardButton(
    text='📆16-21 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=2
    ).pack()
)
button4 = InlineKeyboardButton(
    text='📆23-28 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=3
    ).pack()
)
markup1 = InlineKeyboardMarkup(
    inline_keyboard=[[button1],[button2],[button3],[button4]]
)
button111 = InlineKeyboardButton(
    text='📆02-07 декабряя',
    callback_data=GoodsCallbackFactory(
        category_id=4,
        subcategory_id=0,
        item_id=0
    ).pack()
)


button222 = InlineKeyboardButton(
    text='📆09-14 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=4,
        subcategory_id=0,
        item_id=1
    ).pack()
)
button333 = InlineKeyboardButton(
    text='📆16-21 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=4,
        subcategory_id=0,
        item_id=2
    ).pack()
)
button444 = InlineKeyboardButton(
    text='📆23-28 декабря',
    callback_data=GoodsCallbackFactory(
        category_id=4,
        subcategory_id=0,
        item_id=3
    ).pack()
)
markup4 = InlineKeyboardMarkup(
    inline_keyboard=[[button111],[button222],[button333],[button444]]
)
async def raspinline(indexes,text):
    keyboard = InlineKeyboardBuilder()

    if indexes == []:
        keyboard.add(InlineKeyboardButton(text='💤Выходной', callback_data='5'))
    for index in indexes:
        keyboard.add(InlineKeyboardButton(text=text[index+1],callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index+2],callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index + 3], callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index + 4], callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index + 5], callback_data='5'))
    return keyboard.adjust(5).as_markup()

async def raspinline1(indexes,text):
    keyboard = InlineKeyboardBuilder()

    if indexes == []:
        keyboard.add(InlineKeyboardButton(text='💤Выходной', callback_data='5'))
    for index in indexes:
        keyboard.add(InlineKeyboardButton(text=text[index-3],callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index-2],callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index -1], callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index -4], callback_data='5'))
        keyboard.add(InlineKeyboardButton(text=text[index + 1], callback_data='5'))
    return keyboard.adjust(5).as_markup()