import datetime
import os
import random
from time import sleep
import pandas as pd
import pyrebase
from aiogram import Dispatcher,Bot,types,executor
bot=Bot(token='5842402640:AAEyy0s4-6zl7MZ7OxOcaoairvTRAgPF8lY')
dp=Dispatcher(bot)


firebaseConfig={
"apiKey": "AIzaSyD_ELfpFmQTgpGBwzG5oEsU-m0CbWd3ZHg",
  "authDomain": "mybase-341d1.firebaseapp.com",
  "projectId": "mybase-341d1",
  "storageBucket": "mybase-341d1.appspot.com",
  "messagingSenderId": "73297747191",
  "appId": "1:73297747191:web:2f4fcc8ad1b0f045f9c7f2",
  "measurementId": "G-LB3XJ1ZVKS",
    "databaseURL":"https://mybase-341d1-default-rtdb.firebaseio.com"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

random_quests_numbers = []
index_num = 0
hour = 0
minute = 0
secund = 0
quest = 0
a_option = 0
b_option = 0
c_option = 0
d_option = 0
is_time_finished = False

try:

    start_test=types.InlineKeyboardButton(text='Testni Boshlash✅',callback_data='tstart')
    start_test_markup=types.InlineKeyboardMarkup().add(start_test)
    this_user_access=''
    this_user=''
    len_u=len(db.child('Users').get().val().keys())+1
    user_id=0
    @dp.message_handler(commands=['start'])
    async def start(message:types.Message):

        random_quests_numbers = []
        index_num = 0
        hour = 0
        minute = 0
        secund = 0
        quest = 0
        a_option = 0
        b_option = 0
        c_option = 0
        d_option = 0
        is_time_finished = False
        global db
        global this_user
        global this_user_access
        global len_u
        global start_test_markup
        global user_id
        user_id=message.from_user.id
        len_u=len(db.child('Users').get().val().keys())+1
        is_equal=False
        for i in range(2,len_u):
            checkingUserAccess=db.child('Users').child('u'+str(i)).child('id').get().val()
            if checkingUserAccess==message.from_user.id:
                is_equal=True
                break
            else:
                is_equal=False
        if is_equal:
            this_user_access=db.child('Users').child('u' + str(i)).child('access').get().val()
            this_user = 'u'+str(i)
        if is_equal==False:
            db.child('Users').child('u' + str(len_u)).set({"name":message.from_user.first_name,'id':message.from_user.id,"access":"false",'num':len_u,'mon':datetime.datetime.now().month+1,'day':datetime.datetime.now().day,'math':'false','bt':'false','ova':'false'})
            this_user_access=db.child('Users').child('u' + str(len_u)).child('access').get().val()
            this_user='u'+str(len_u)
        await message.answer(
            "Assalomu alaykum ustoz agar siz Attestatsiga tayyorgarlik ko'rmoqchi bo'lsangiz biz bilan bilimingizni oshirishingiz mumkin biz sizga professional testlarni taqdim etamiz, bot sizda ishlashligi  uchun  @Wunderkinds_admin ga murojaat eting!\n\n"
            f"Tartib Raqamingiz: {len_u-1}\n\n"
            f"Sizning ID: {user_id}\n\n"
            'Tel: 👇👇 \n'
            '+998 91 121 23 99\n'
            "+998 90 056 79 93"
            ,
            reply_markup=start_test_markup
        )

    #
    #
    # stest_math=types.InlineKeyboardButton(text='Matematika',callback_data='math_start')
    # stest_phy=types.InlineKeyboardButton(text='Ona tili va Adabiyot',callback_data='phy_start')
    # bosh_talim=types.InlineKeyboardButton(text="Boshlang'ich Talim",callback_data='bsht')
    # start_kb_mk=types.InlineKeyboardMarkup(row_width=2).add(stest_math,stest_phy,bosh_talim)
    #
    # Matematika start test btn
    only_math_access_btn=types.InlineKeyboardButton(text='Boshlash',callback_data='only_math')
    math_access_kb=types.InlineKeyboardMarkup().add(only_math_access_btn)

    # ona tili va adabiyot start test btn
    only_ova_access_btn=types.InlineKeyboardButton(text='Boshlash',callback_data='only_ova')
    ova_access_kb=types.InlineKeyboardMarkup().add(only_ova_access_btn)

    only_bt_access_btn=types.InlineKeyboardButton(text='Boshlash',callback_data='only_bt')
    bt_access_kb=types.InlineKeyboardMarkup().add(only_bt_access_btn)

    user=''

    @dp.callback_query_handler(text='tstart')
    async def tstartfun(call:types.CallbackQuery):
        global len_u,user
        global math_access_kb
        len_users= list(db.child('Users').get().val().keys())
        math_access=''
        bt_access=''
        ova_access=''
        for i in range(2,len(len_users)+1):
            thisuser=db.child('Users').child('u'+str(i)).child('id').get().val()
            if thisuser==call.from_user.id:
                math_access = db.child('Users').child('u' + str(i)).child('math').get().val()
                bt_access = db.child('Users').child('u' + str(i)).child('bt').get().val()
                ova_access = db.child('Users').child('u' + str(i)).child('ova').get().val()
                user='u' + str(i)
                break

        if math_access=='true':
            await call.message.edit_text(
                "Matematika Fanidan Attestatsiya Testlar .\n"
                "❗️❗️Eslatib O'tamiz : \n\n"
                "⏰ Sizga 80 daqiqa vaqt beriladi\n"
                "80 daqiqadan so'ng test avtomatik tarzda tugatiladi ❗\n\n"
                "Agar Test Yechish Mobaynida Chiqib Ketib Qolsangiz Test Avtomatik Tugatiladi ❗"
                ,reply_markup=math_access_kb
            )
        if bt_access=='true':
            await call.message.edit_text(
                "Boshlang'ich Talim Attestatsiya Testlar .\n"
                "❗️❗️Eslatib O'tamiz : \n\n"
                "⏰ Sizga 60 daqiqa vaqt beriladi\n"
                "60 daqiqadan so'ng test avtomatik tarzda tugatiladi ❗\n\n"
                "Agar Test Yechish Mobaynida Chiqib Ketib Qolsangiz Test Avtomatik Tugatiladi ❗"
                ,reply_markup=bt_access_kb
            )
        if ova_access=='true':
            await call.message.edit_text(
                "Ona tili va Adabiyot Fanidan Attestatsiya Testlar .\n"
                "❗️❗️Eslatib O'tamiz : \n\n"
                "⏰ Sizga 60 daqiqa vaqt beriladi\n"
                "60 daqiqadan so'ng test avtomatik tarzda tugatiladi ❗\n\n"
                "Agar Test Yechish Mobaynida Chiqib Ketib Qolsangiz Test Avtomatik Tugatiladi ❗"
                ,reply_markup=ova_access_kb
            )



        if math_access=='false' and bt_access=='false' and ova_access=='false':
            await call.message.answer(
                "Botdan foydalanish uchun @Wunderkinds_admin ga murojat qiling:\n\n"
                "Qo`ng`iroq qiling\n\n"
                "☎️+998 91 121 23 99\n\n"
                "☎️+998 90 056 79 93\n\n"
                "👆 👆 👆 👆\n\n"
                "Admin Sizga Foydalanish Huhuqini Bergandan So'ng ' Testni Boshlash✅ ' Tugmasini Bosing"
            )










    a_ans_true=types.InlineKeyboardButton(text='A',callback_data='ans_a')
    b_ans_true=types.InlineKeyboardButton(text='B',callback_data='ans_b')
    c_ans_true=types.InlineKeyboardButton(text='C',callback_data='ans_c')
    d_ans_true=types.InlineKeyboardButton(text='D',callback_data='ans_d')
    next_quest=types.InlineKeyboardButton(text='Keyingi Savol',callback_data='next_quest')
    answer_select_kb=types.InlineKeyboardMarkup(row_width=2).add(a_ans_true,b_ans_true,c_ans_true,d_ans_true,next_quest)


    true_ans_count=0
    # OvA buttons(Ona Tili va Adabiyot)
    ova_a_ans_true=types.InlineKeyboardButton(text='A',callback_data='ova_ans_a')
    ova_b_ans_true=types.InlineKeyboardButton(text='B',callback_data='ova_ans_b')
    ova_c_ans_true=types.InlineKeyboardButton(text='C',callback_data='ova_ans_c')
    ova_d_ans_true=types.InlineKeyboardButton(text='D',callback_data='ova_ans_d')
    ova_next_quest=types.InlineKeyboardButton(text='Keyingi Savol',callback_data='ova_next_quest')
    ova_answer_select_kb=types.InlineKeyboardMarkup(row_width=2).add(ova_a_ans_true,ova_b_ans_true,ova_c_ans_true,ova_d_ans_true,ova_next_quest)


    #  BT button (Boshlang'ich talim)
    bt_a_ans_true=types.InlineKeyboardButton(text='A',callback_data='bt_ans_a')
    bt_b_ans_true=types.InlineKeyboardButton(text='B',callback_data='bt_ans_b')
    bt_c_ans_true=types.InlineKeyboardButton(text='C',callback_data='bt_ans_c')
    bt_d_ans_true=types.InlineKeyboardButton(text='D',callback_data='bt_ans_d')
    bt_next_quest=types.InlineKeyboardButton(text='Keyingi Savol',callback_data='bt_next_quest')
    bt_answer_select_kb=types.InlineKeyboardMarkup(row_width=2).add(bt_a_ans_true,bt_b_ans_true,bt_c_ans_true,bt_d_ans_true,bt_next_quest)



    @dp.callback_query_handler(text=['only_math','only_ova','only_bt'])
    async def onlyMath(call:types.CallbackQuery):
        global random_quests_numbers
        global hour
        global minute
        global secund
        global is_closed_math
        global answer_select_kb
        global quest
        global a_option
        global b_option
        global c_option
        global d_option
        global quest,this_user
        global is_time_finished,start_test_markup
        if db.child('Users').child(this_user).child('day').get().val()==datetime.datetime.now().day and db.child('Users').child(this_user).child('mon').get().val()==datetime.datetime.now().month:
            db.child('Users').child(this_user).update({'math': 'false', 'bt': 'false', 'ova': 'false'})
            await call.message.edit_text(
                "Sizning obunangizni vaqti Tugatildi. Botdan 1-oy davomida faydalanishingiz mumkun\n"
                "Qayta ishga tushirish uchun Adminga Bo'glaning !\n\n"
                f"Tartib Raqamingiz: {len_u - 1}\n\n"
                f"Sizning ID: {user_id}\n\n"
                'Tel: 👇👇 \n'
                '+998 91 121 23 99',
                reply_markup=start_test_markup
            )
        else:
            if call.data == 'only_math':
                tests_len = len(db.child('tests').child('matematika').get().val().keys())
                random_quests_numbers = []
                for i in range(1, 100):
                    random_num = random.randint(1, tests_len - 2)
                    if random_num not in random_quests_numbers:
                        random_quests_numbers.append(random_num)
                    else:
                        random_num = random.randint(random_num, tests_len - 2)
                        if random_num not in random_quests_numbers:
                            random_quests_numbers.append(random_num)
                    if len(random_quests_numbers) == 40:
                        break

                quest = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                    'quest').child('name').get().val()
                a_option = db.child('tests').child('matematika').child(
                    't' + str(random_quests_numbers[index_num])).child('a').child('option').get().val()
                b_option = db.child('tests').child('matematika').child(
                    't' + str(random_quests_numbers[index_num])).child('b').child('option').get().val()
                c_option = db.child('tests').child('matematika').child(
                    't' + str(random_quests_numbers[index_num])).child('c').child('option').get().val()
                d_option = db.child('tests').child('matematika').child(
                    't' + str(random_quests_numbers[index_num])).child('d').child('option').get().val()

                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute + 80

                await call.message.answer(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=answer_select_kb
                )

                while True:
                    await call.message.edit_text(
                        f"Qolgan Vaqtingiz:{hour - datetime.datetime.now().hour}:{minute - datetime.datetime.now().minute}:{60 - datetime.datetime.now().second}"
                    )
                    await call.message.pin(disable_notification=True)
                    sleep(1)
                    if hour - datetime.datetime.now().hour <= 0:
                        if minute - datetime.datetime.now().minute <= 0:
                            if datetime.datetime.now().second > 55:
                                await call.message.answer(
                                    "Vaqtingiz Tugagan\n\n"
                                    f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                                    f"Tog'ri Javob : {true_ans_count}"
                                )
                                is_time_finished = True
                                break

            if call.data == 'only_ova':
                tests_len = len(db.child('tests').child('ova').get().val().keys())
                random_quests_numbers = []
                for i in range(1, 100):
                    random_num = random.randint(1, tests_len - 2)
                    if random_num not in random_quests_numbers:
                        random_quests_numbers.append(random_num)
                    else:
                        random_num = random.randint(random_num, tests_len - 2)
                        if random_num not in random_quests_numbers:
                            random_quests_numbers.append(random_num)
                    if len(random_quests_numbers) == 40:
                        break

                quest = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                    'quest').child('name').get().val()
                a_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                    'a').child('option').get().val()
                b_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                    'b').child('option').get().val()
                c_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                    'c').child('option').get().val()
                d_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                    'd').child('option').get().val()

                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute + 60

                await call.message.answer(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=ova_answer_select_kb
                )

                while True:
                    await call.message.edit_text(
                        f"Qolgan Vaqtingiz:{hour - datetime.datetime.now().hour}:{minute - datetime.datetime.now().minute}:{60 - datetime.datetime.now().second}"
                    )
                    await call.message.pin(disable_notification=True)
                    sleep(1)
                    if hour - datetime.datetime.now().hour <= 0:
                        if minute - datetime.datetime.now().minute <= 0:
                            if datetime.datetime.now().second > 55:
                                await call.message.answer(
                                    "Vaqtingiz Tugagan\n\n"
                                    f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                                    f"Tog'ri Javob : {true_ans_count}\n\n"
                                    "Tesni qayta boshlash uchun /start ni bosing."
                                )
                                is_time_finished = True
                                break

            if call.data == 'only_bt':
                tests_len = len(db.child('tests').child('boshtalim').get().val().keys())
                random_quests_numbers = []
                for i in range(1, 100):
                    random_num = random.randint(1, tests_len - 2)
                    if random_num not in random_quests_numbers:
                        random_quests_numbers.append(random_num)
                    else:
                        random_num = random.randint(random_num, tests_len - 2)
                        if random_num not in random_quests_numbers:
                            random_quests_numbers.append(random_num)
                    if len(random_quests_numbers) == 40:
                        break

                quest = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                    'quest').child('name').get().val()
                a_option = db.child('tests').child('boshtalim').child(
                    't' + str(random_quests_numbers[index_num])).child(
                    'a').child('option').get().val()
                b_option = db.child('tests').child('boshtalim').child(
                    't' + str(random_quests_numbers[index_num])).child(
                    'b').child('option').get().val()
                c_option = db.child('tests').child('boshtalim').child(
                    't' + str(random_quests_numbers[index_num])).child(
                    'c').child('option').get().val()
                d_option = db.child('tests').child('boshtalim').child(
                    't' + str(random_quests_numbers[index_num])).child(
                    'd').child('option').get().val()

                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute + 60

                await call.message.answer(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=bt_answer_select_kb
                )

                while True:
                    await call.message.edit_text(
                        f"Qolgan Vaqtingiz:{hour - datetime.datetime.now().hour}:{minute - datetime.datetime.now().minute}:{60 - datetime.datetime.now().second}"
                    )
                    await call.message.pin()
                    sleep(1)
                    if hour - datetime.datetime.now().hour <= 0:
                        if minute - datetime.datetime.now().minute <= 0:
                            if datetime.datetime.now().second > 55:
                                await call.message.answer(
                                    "Vaqtingiz Tugagan\n\n"
                                    f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                                    f"Tog'ri Javob : {true_ans_count}\n\n"
                                    "Tesni qayta boshlash uchun /start ni bosing."
                                )
                                is_time_finished = True
                                break




    # Boshlang'ich Ta'lim




    bt_a_selected=False
    bt_b_selected=False
    bt_c_selected=False
    bt_d_selected=False
    @dp.callback_query_handler(text=["bt_ans_a","bt_ans_b","bt_ans_c","bt_ans_d","bt_next_quest"])
    async def AnswerChecker(call:types.CallbackQuery):
        global quest,true_ans_count
        global a_option,b_option,c_option,d_option
        global is_time_finished
        global a_selected,b_selected,c_selected,d_selected
        global index_num
        if is_time_finished!=True and index_num<41:
            if call.data=='bt_ans_a':
                a_selected = True
                b_selected = False
                c_selected = False
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option} ✅\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=bt_answer_select_kb
                )
            if call.data=='bt_ans_b':
                a_selected = False
                b_selected = True
                c_selected = False
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option} ✅\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=bt_answer_select_kb
                )
            if call.data=='bt_ans_c':
                a_selected = False
                b_selected = False
                c_selected = True
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option} ✅\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=bt_answer_select_kb
                )
            if call.data=='bt_ans_d':
                a_selected = False
                b_selected = False
                c_selected = False
                d_selected = True
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option} ✅\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=bt_answer_select_kb
                )
            if call.data=='bt_next_quest':

                a_check = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child('a').child(
                    'trust').get().val()
                b_check = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child('b').child(
                    'trust').get().val()
                c_check = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child('c').child(
                    'trust').get().val()
                d_check = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child('d').child(
                    'trust').get().val()
                if a_selected==True:
                    if a_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if b_selected==True:
                    if b_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if c_selected==True:
                    if c_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if d_selected==True:
                    if d_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if a_selected==False and b_selected==False and c_selected==False and d_selected==False:
                    await call.message.edit_text(
                        f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n❗️Variyantlardan Birini Tanlamasangiz Keyingi Savolga o'ta olmaysiz❗️\n\nJavobingizni Tanlang: \n",
                        reply_markup=bt_answer_select_kb
                    )

                else:
                    if index_num!=39:
                        index_num+=1
                        quest = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                            'quest').child('name').get().val()
                        a_option = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                            'a').child('option').get().val()
                        b_option = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                            'b').child('option').get().val()
                        c_option = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                            'c').child('option').get().val()
                        d_option = db.child('tests').child('boshtalim').child('t' + str(random_quests_numbers[index_num])).child(
                            'd').child('option').get().val()
                        await call.message.edit_text(
                            f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                            reply_markup=bt_answer_select_kb
                        )
                    else:
                        await call.message.edit_text(
                            "Vaqtingiz Allaqachon Tugagan\n\n"
                            f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                            f"Tog'ri Javob : {true_ans_count}\n"
                            f"To'plagan Balingiz: {true_ans_count * 2} ball"
                            "Tesni qayta boshlash uchun /start ni bosing."

                        )






        else:
            await call.message.edit_text(
                "Vaqtingiz Allaqachon Tugagan\n\n"
                f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                f"Tog'ri Javob : {true_ans_count}\n"
                f"To'plagan Balingiz: {true_ans_count*2} ball"
                "Tesni qayta boshlash uchun /start ni bosing."

            )









    # OvA(Ona tili va Adabiyot)


    ova_a_selected=False
    ova_b_selected=False
    ova_c_selected=False
    ova_d_selected=False
    @dp.callback_query_handler(text=["ova_ans_a","ova_ans_b","ova_ans_c","ova_ans_d",'ova_next_quest'])
    async def AnswerCheckerOVA(call:types.CallbackQuery):
        global quest,true_ans_count
        global a_option,b_option,c_option,d_option
        global is_time_finished
        global ova_a_selected,ova_b_selected,ova_c_selected,ova_d_selected
        global index_num
        if is_time_finished!=True and index_num!=41:
            if call.data=='ova_ans_a':
                ova_a_selected = True
                ova_b_selected = False
                ova_c_selected = False
                ova_d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option} ✅\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=ova_answer_select_kb
                )
            if call.data=='ova_ans_b':
                ova_a_selected = False
                ova_b_selected = True
                ova_c_selected = False
                ova_d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option} ✅\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=ova_answer_select_kb
                )
            if call.data=='ova_ans_c':
                ova_a_selected = False
                ova_b_selected = False
                ova_c_selected = True
                ova_d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option} ✅\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=ova_answer_select_kb
                )
            if call.data=='ova_ans_d':
                ova_a_selected = False
                ova_b_selected = False
                ova_c_selected = False
                ova_d_selected = True
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option} ✅\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=ova_answer_select_kb
                )
            if call.data=='ova_next_quest':
                ova_a_check = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child('a').child(
                    'trust').get().val()
                ova_b_check = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child('b').child(
                    'trust').get().val()
                ova_c_check = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child('c').child(
                    'trust').get().val()
                ova_d_check = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child('d').child(
                    'trust').get().val()
                if ova_a_selected==True:
                    if ova_a_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if ova_b_selected==True:
                    if ova_b_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if ova_c_selected==True:
                    if ova_c_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if ova_d_selected==True:
                    if ova_d_check=='true':
                        true_ans_count+=1
                    else:
                        pass
                if ova_a_selected==False and ova_b_selected==False and ova_c_selected==False and ova_d_selected==False:
                    await call.message.edit_text(
                        f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n❗️Variyantlardan Birini Tanlamasangiz Keyingi Savolga o'ta olmaysiz❗️\n\nJavobingizni Tanlang: \n",
                        reply_markup=ova_answer_select_kb
                    )

                else:
                    index_num+=1
                    quest = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                        'quest').child('name').get().val()
                    a_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                        'a').child('option').get().val()
                    b_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                        'b').child('option').get().val()
                    c_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                        'c').child('option').get().val()
                    d_option = db.child('tests').child('ova').child('t' + str(random_quests_numbers[index_num])).child(
                        'd').child('option').get().val()


                    await call.message.edit_text(
                        f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                        reply_markup=ova_answer_select_kb
                    )








        else:
            await call.message.edit_text(
                "Vaqtingiz Allaqachon Tugagan\n\n"
                f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                f"Tog'ri Javob : {true_ans_count}\n\n"
                f"To'plagan Balingiz: {true_ans_count*2} ball"
                "Tesni qayta boshlash uchun /start ni bosing."

            )














    # Math

    a_selected=False
    b_selected=False
    c_selected=False
    d_selected=False
    @dp.callback_query_handler(text=["ans_a","ans_b","ans_c","ans_d",'next_quest'])
    async def AnswerCheckerMath(call:types.CallbackQuery):
        global quest, true_ans_count
        global a_option, b_option, c_option, d_option
        global is_time_finished
        global a_selected, b_selected,c_selected,d_selected
        global index_num
        if is_time_finished != True and index_num != 41:
            if call.data == 'ans_a':
                a_selected = True
                b_selected = False
                c_selected = False
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option} ✅\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=answer_select_kb
                )
            if call.data == 'ans_b':
                a_selected = False
                b_selected = True
                c_selected = False
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option} ✅\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=answer_select_kb
                )
            if call.data == 'ans_c':
                a_selected = False
                b_selected = False
                c_selected = True
                d_selected = False
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option} ✅\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=answer_select_kb
                )
            if call.data == 'ans_d':
                a_selected = False
                b_selected = False
                c_selected = False
                d_selected = True
                await call.message.edit_text(
                    f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option} ✅\n\n\n\nJavobingizni Tanlang: \n",
                    reply_markup=answer_select_kb
                )
            if call.data == 'next_quest':
                a_check = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                    'a').child(
                    'trust').get().val()
                b_check = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                    'b').child(
                    'trust').get().val()
                c_check = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                    'c').child(
                    'trust').get().val()
                d_check = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                    'd').child(
                    'trust').get().val()
                if a_selected == True:
                    if a_check == 'true':
                        true_ans_count += 1
                    else:
                        pass
                if b_selected == True:
                    if b_check == 'true':
                        true_ans_count += 1
                    else:
                       pass
                if ova_c_selected == True:
                    if c_check == 'true':
                        true_ans_count += 1
                    else:
                        pass
                if ova_d_selected == True:
                    if d_check == 'true':
                        true_ans_count += 1
                    else:
                        pass
                if a_selected == False and b_selected == False and c_selected == False and d_selected == False:
                    await call.message.edit_text(
                        f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n❗️Variyantlardan Birini Tanlamasangiz Keyingi Savolga o'ta olmaysiz❗️\n\nJavobingizni Tanlang: \n",
                        reply_markup=answer_select_kb
                    )

                else:
                    index_num += 1
                    quest = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                        'quest').child('name').get().val()
                    a_option = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                        'a').child('option').get().val()
                    b_option = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                        'b').child('option').get().val()
                    c_option = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                        'c').child('option').get().val()
                    d_option = db.child('tests').child('matematika').child('t' + str(random_quests_numbers[index_num])).child(
                        'd').child('option').get().val()

                    await call.message.edit_text(
                        f"[{index_num + 1}/40]\nSavol : {quest}\n\nA: {a_option}\nB: {b_option}\nC: {c_option}\nD: {d_option}\n\n\n\nJavobingizni Tanlang: \n",
                        reply_markup=answer_select_kb
                    )








        else:
            await call.message.edit_text(
                "Vaqtingiz Allaqachon Tugagan\n\n"
                f"Jami Testlar :{len(random_quests_numbers)}\n\n"
                f"Tog'ri Javob : {true_ans_count}\n\n"
                f"To'plagan Balingiz: {true_ans_count * 2} ball"
                "Tesni qayta boshlash uchun /start ni bosing."

            )






























































    ###############
    ###############         ADmin panel
    ###############

    ###################             ADMIN PANEL         ###################

    ###Buttons for Admin Panel Menu

    requsted_mems=types.InlineKeyboardButton(text="Ruxsat So'raganlar ✅",callback_data='requested_mems')
    new_test=types.InlineKeyboardButton(text="Yangi Test Qo'shish ➕",callback_data='newtest')
    exit_admin_panel=types.InlineKeyboardButton(text='⬅️Admin Paneldan Chiqish',callback_data='exit_admin_panel')
    rp_admin_kb=types.InlineKeyboardMarkup(row_width=2).add(requsted_mems,new_test,exit_admin_panel)



    ### listen user's text to enter admin panel
    acces_doc_get=False
    @dp.message_handler()
    async def AdminPanel(message:types.Message):
        global rp_admin_kb
        global start_test_markup
        global len_u
        global acces_doc_get
        # variable text equal to user's text message
        text=message.text


        #check text / if text equal to Admin password(Admin123)



        if text=='93991':
            acces_doc_get=True
            await message.answer(
                "Admin Panel: \n\n"
                "Kerakli Bo'limni Tanlang: \n"
                , reply_markup=rp_admin_kb
            )






    ##  Button for ruturn admin panel
    exit_req_users_list=types.InlineKeyboardButton(text='Back◀️',callback_data='backtoAdminPanel')

    #///////////////////////////////////    Buttons for Create New Test ////////////////////////////////////#
    math_selected=types.InlineKeyboardButton(text='Matematika',callback_data='math_s')
    ova_selected=types.InlineKeyboardButton(text='Ona Tili va Adabiyot',callback_data='ova_s')
    bosh_talim_selected=types.InlineKeyboardButton(text="Boshlang'ich Ta'lim",callback_data='bosh_talim_s')
    selected_category=types.InlineKeyboardMarkup(row_width=1).add(math_selected,ova_selected,bosh_talim_selected,exit_req_users_list)


    ###############  check admin menu buttons (clicked or not)

    @dp.callback_query_handler(text=['requested_mems','newtest','exit_admin_panel'])
    async def checkAdminPanelButtons(call:types.CallbackQuery):
        global selected_category
        global user_id
        data=call.data
        len_reqs = len(db.child('Users').get().val().keys())
        users = ''
        rp_markup=types.InlineKeyboardMarkup(row_width=3)
        if data=='requested_mems':
            a_len=0;
            for i in range(2,len_reqs+1):
                name=db.child("Users").child('u'+str(i)).child('name').get().val()
                id=db.child("Users").child('u'+str(i)).child('id').get().val()
                num=db.child('Users').child('u'+str(i)).child('num').get().val()
                users+=f'{num}. Name: {name} id: {id}\n\n'
                rp_markup.add(types.InlineKeyboardButton(text=str(num),callback_data=f'u{num}'))
                a_len+=1
            rp_markup.add(exit_req_users_list)
            await call.message.edit_text(
                "Rexsat Soraganlar:\n\n"
                f"Jami: {a_len} ta\n\n"
               f"{users}",
                reply_markup=rp_markup
            )
        if data=='newtest':
            await call.message.edit_text(
                "Qaysi fan uchun test tuzmoqchisiz ? : ",
                reply_markup=selected_category
            )

        if data=='exit_admin_panel':
            await call.message.edit_text(
                "Assalomu alaykum ustoz agar siz Boshlang'ich sinf ustozi bo'lsangiz biz bilan bilimingizni oshirishingiz mumkin biz sizga professional testlarni taqdim etamiz, bot sizda ishlashligi  uchun  @admin_name ga murojaat eting!\n\n"
                f"Tartib Raqamingiz: {len_u - 1}\n\n"
                f"Sizning ID: {user_id}\n\n"
                'Tel: 👇👇 \n'
                '+998 91 121 23 99',
                reply_markup=start_test_markup
            )




    #/////////////////////////////////////  Add New Test

    @dp.callback_query_handler(text=['math_s'])
    async def AddMathQuest(call:types.CallbackQuery):
        if call.data=="math_s":
            await call.message.edit_text(
                "Menga Exel Fileni Jo'nating "
            )

            @dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
            async def math_handler(message: types.Message):
                if document := message.document:
                    await document.download(
                        destination_file="file.xlsx",
                    )
                    await call.message.edit_text(
                        "Fayl Yuklanmoqda . . .\n\n"
                    )
                exel_data = pd.read_excel('file.xlsx')
                quests = exel_data['Savol'].tolist()
                a = exel_data['A'].tolist()
                b = exel_data['B'].tolist()
                c = exel_data['C'].tolist()
                d = exel_data['D'].tolist()
                true_ans = exel_data['tv'].tolist()
                await call.message.edit_text(
                    "Fayl Yuklandi \n\n"
                    "Bazaga qo'shilmoqda . . . "
                )
                for i in range(0, len(quests)):
                    bt_len = len(db.child('tests').child('matematika').get().val().keys())
                    if true_ans[i].lower() == 'a':
                        db.child('tests').child('matematika').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'true'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'b':
                        db.child('tests').child('matematika').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'true'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'c':
                        db.child('tests').child('matematika').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'true'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'd':
                        db.child('tests').child('matematika').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'true'},
                             'quest': {"name": quests[i]}})
                await call.message.edit_text(
                    "Savollar Bazga Qo'shildi",
                    reply_markup=rp_admin_kb

                )
                os.remove('file.xlsx')

    @dp.callback_query_handler(text=['ova_s'])
    async def newTestAddOvA(call:types.CallbackQuery):
        if call.data=='ova_s':
            await call.message.edit_text(
                "Menga Exel Fileni Jo'nating "
            )

            @dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
            async def ova_handler(message: types.Message):
                if document := message.document:
                    await document.download(
                        destination_file="file.xlsx",
                    )
                    await call.message.edit_text(
                        "Fayl Yuklanmoqda . . .\n\n"
                    )
                exel_data = pd.read_excel('file.xlsx')
                quests = exel_data['Savol'].tolist()
                a = exel_data['A'].tolist()
                b = exel_data['B'].tolist()
                c = exel_data['C'].tolist()
                d = exel_data['D'].tolist()
                true_ans = exel_data['tv'].tolist()
                await call.message.edit_text(
                    "Fayl Yuklandi \n\n"
                    "Bazaga qo'shilmoqda . . . "
                )
                for i in range(0, len(quests)):
                    bt_len = len(db.child('tests').child('ova').get().val().keys())
                    if true_ans[i].lower() == 'a':
                        db.child('tests').child('ova').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'true'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'b':
                        db.child('tests').child('ova').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'true'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'c':
                        db.child('tests').child('ova').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'true'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'd':
                        db.child('tests').child('ova').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'true'},
                             'quest': {"name": quests[i]}})
                await call.message.answer(
                    "Savollar Bazga Qo'shildi",
                    reply_markup=rp_admin_kb

                )
                os.remove('file.xlsx')


    @dp.callback_query_handler(text=['bosh_talim_s'])
    async def newTestAddFunctions(call:types.CallbackQuery):
        data=call.data
        if data=='bosh_talim_s':
            await call.message.edit_text(
                "Menga Exel Fileni Jo'nating "
            )
            @dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
            async def bt_handler(message: types.Message):
                if document := message.document:
                    await document.download(
                        destination_file="file.xlsx",
                    )
                    await call.message.edit_text(
                        "Fayl Yuklanmoqda . . .\n\n"
                    )
                exel_data = pd.read_excel('file.xlsx')
                quests = exel_data['Savol'].tolist()
                a = exel_data['A'].tolist()
                b = exel_data['B'].tolist()
                c = exel_data['C'].tolist()
                d = exel_data['D'].tolist()
                true_ans = exel_data['tv'].tolist()
                await call.message.edit_text(
                    "Fayl Yuklandi \n\n"
                    "Bazaga qo'shilmoqda . . . "
                )
                for i in range(0, len(quests)):
                    bt_len = len(db.child('tests').child('boshtalim').get().val().keys())
                    if true_ans[i].lower() == 'a':
                        db.child('tests').child('boshtalim').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'true'}, 'b': {"option": b[i], "trust": 'false'},'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'b':
                        db.child('tests').child('boshtalim').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'true'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'c':
                        db.child('tests').child('boshtalim').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'true'}, 'd': {"option": d[i], "trust": 'false'},
                             'quest': {"name": quests[i]}})
                    if true_ans[i].lower() == 'd':
                        db.child('tests').child('boshtalim').child('t' + str(bt_len - 1)).set(
                            {'a': {"option": a[i], "trust": 'false'}, 'b': {"option": b[i], "trust": 'false'},
                             'c': {"option": c[i], "trust": 'false'}, 'd': {"option": d[i], "trust": 'true'},
                             'quest': {"name": quests[i]}})
                await call.message.edit_text(
                    "Savollar Bazga Qo'shildi",
                    reply_markup=rp_admin_kb

                )
                os.remove('file.xlsx')






    #########   Requested Users Edit Menu



    rmv=types.InlineKeyboardButton(text="O'chirib yuborish ❌",callback_data='rmv')
    math_true=types.InlineKeyboardButton(text='Matematika',callback_data='math_true')
    bt_true=types.InlineKeyboardButton(text="Boshlang'ich talim",callback_data='bt_true')
    ova_true=types.InlineKeyboardButton(text='Ona Tili va Adabiyt',callback_data='ova_true')

    reply_edit_user=types.InlineKeyboardMarkup(row_width=1).add(math_true,bt_true,ova_true,rmv,exit_req_users_list)

    user=''
    @dp.callback_query_handler()
    async def handlers(call:types.CallbackQuery):
        global user
        global reply_edit_user
        global rp_admin_kb
        try:
            if call.data[:1]=='u' and int(call.data[1:]) > 0 :
                name=db.child("Users").child(str(call.data)).child('name').get().val()
                id=db.child("Users").child(str(call.data)).child('id').get().val()
                num=db.child("Users").child(str(call.data)).child('num').get().val()
                mon=db.child('Users').child(str(call.data)).child('mon').get().val()
                day=db.child('Users').child(str(call.data)).child('day').get().val()
                math_solv=db.child('Users').child(str(call.data)).child('math').get().val()
                bt_solv=db.child('Users').child(str(call.data)).child('bt').get().val()
                ova_solv=db.child('Users').child(str(call.data)).child('ova').get().val()

                user=call.data
                await call.message.edit_text(
                    f"\nTartib Raqami:{num}\n"
                    f"Name: {name}\n\n"
                    f"id : {id}\n\n"
                    f"O'cirib Tashlash Sanasi: {mon}-oy, {day}-kun\n\n"
                    f"Matematika -- {math_solv} \n\n"
                    f"Ona Tili va Adabiyot -- {ova_solv}\n\n"
                    f"Boshlang'ich Talim -- {bt_solv}"
                    ,reply_markup=reply_edit_user
                )

            if call.data=='math_true':
                one_time_math=False
                if db.child("Users").child(user).child('math').get().val()=='false':
                    db.child("Users").child(user).update({'math':'true'})
                    db.child("Users").child(user).update({'ova':'false'})
                    db.child("Users").child(user).update({'bt':'false'})

                    one_time_math=True
                elif db.child("Users").child(user).child('math').get().val() == 'true':
                    db.child("Users").child(user).update({'math': 'false'})
                    db.child("Users").child(user).update({'ova': 'false'})
                    db.child("Users").child(user).update({'bt': 'false'})
                    one_time_math=False
                uname = db.child("Users").child(str(user)).child('name').get().val()
                uid = db.child("Users").child(str(user)).child('id').get().val()
                unum = db.child("Users").child(str(user)).child('num').get().val()
                umon = db.child('Users').child(str(user)).child('mon').get().val()
                uday = db.child('Users').child(str(user)).child('day').get().val()
                umath_solv = db.child('Users').child(str(user)).child('math').get().val()
                ubt_solv = db.child('Users').child(str(user)).child('bt').get().val()
                uova_solv = db.child('Users').child(str(user)).child('ova').get().val()
                await call.message.edit_text(
                            f"\nTartib Raqami: {unum}\n"
                            f"Name: {uname}\n\n"
                            f"id : {uid}\n\n"
                            f"O'cirib Tashlash Sanasi: {umon}-oy, {uday}-kun\n\n"
                            f"Matematika -- {one_time_math} \n\n"
                            f"Ona Tili va Adabiyot -- {uova_solv}\n\n"
                            f"Boshlang'ich Talim -- {ubt_solv}"
                            ,reply_markup=reply_edit_user
                        )
            if call.data == 'bt_true':
                one_time_bt=False
                if db.child("Users").child(user).child('bt').get().val()=='false':
                    db.child("Users").child(user).update({'bt':'true'})
                    db.child("Users").child(user).update({'math': 'false'})
                    db.child("Users").child(user).update({'ova': 'false'})

                    one_time_bt=True
                elif db.child("Users").child(user).child('bt').get().val() == 'true':
                    db.child("Users").child(user).update({'bt': 'false'})
                    db.child("Users").child(user).update({'math': 'false'})
                    db.child("Users").child(user).update({'ova': 'false'})
                    one_time_bt=False
                suname = db.child("Users").child(str(user)).child('name').get().val()
                suid = db.child("Users").child(str(user)).child('id').get().val()
                sunum = db.child("Users").child(str(user)).child('num').get().val()
                smon = db.child('Users').child(str(user)).child('mon').get().val()
                sday = db.child('Users').child(str(user)).child('day').get().val()
                smath_solv = db.child('Users').child(str(call.data)).child('math').get().val()
                sbt_solv = db.child('Users').child(str(call.data)).child('bt').get().val()
                sova_solv = db.child('Users').child(str(call.data)).child('ova').get().val()
                await call.message.edit_text(
                    f"Name: {suname}\n\n"
                    f"Tartib Raqami: {sunum}\n"
                    f"id : {suid}\n"
                    f"O'cirib Tashlash Sanasi: {smon}-oy, {sday}-kun\n\n"
                    f"Matematika -- {smath_solv} \n"
                    f"Ona Tili va Adabiyot -- {sova_solv}\n"
                    f"Boshlang'ich Talim -- {one_time_bt}\n"
                    , reply_markup=reply_edit_user
                )
            if call.data == 'ova_true':
                one_time_ova=False
                if db.child("Users").child(user).child('ova').get().val()=='false':
                    db.child("Users").child(user).update({'ova':'true'})
                    db.child("Users").child(user).update({'math': 'false'})
                    db.child("Users").child(user).update({'bt': 'false'})
                    one_time_ova=True
                elif db.child("Users").child(user).child('ova').get().val() == 'true':
                    db.child("Users").child(user).update({'ova': 'false'})
                    db.child("Users").child(user).update({'math': 'false'})
                    db.child("Users").child(user).update({'bt': 'false'})
                    one_time_ova=False
                ouname = db.child("Users").child(str(user)).child('name').get().val()
                ouid = db.child("Users").child(str(user)).child('id').get().val()
                ounum = db.child("Users").child(str(user)).child('num').get().val()
                omon = db.child('Users').child(str(user)).child('mon').get().val()
                oday = db.child('Users').child(str(user)).child('day').get().val()
                omath_solv = db.child('Users').child(str(call.data)).child('math').get().val()
                obt_solv = db.child('Users').child(str(call.data)).child('bt').get().val()
                oova_solv = db.child('Users').child(str(call.data)).child('ova').get().val()
                await call.message.edit_text(

                    f"Name: {ouname}\n\n"
                    f"Tartib Raqami: {ounum}\n\n"
                    f"id : {ouid}\n\n"
                    f"O'cirib Tashlash Sanasi: {omon}-oy, {oday}-kun\n\n"
                    f"Matematika -- {omath_solv} \n\n"
                    f"Ona Tili va Adabiyot -- {one_time_ova}\n\n"
                    f"Boshlang'ich Talim -- {obt_solv}"
                    , reply_markup=reply_edit_user
                )
            if call.data=='rmv':
                db.child("Users").child(user).remove()
                await call.message.edit_text("Muvofiqatli O'cirib Tashlandi\n\nAsosiy Menu: ",reply_markup=rp_admin_kb)
            if call.data=='backtoAdminPanel':
                await call.message.edit_text(
                    "Admin Panel :",
                    reply_markup=rp_admin_kb
                )


        except:
            await call.message.edit_text(
                "Nimadur Xato Bo'ldi !\n"
                "Iltimos Qayta Urining🔁\n",
                reply_markup=rp_admin_kb
            )

except:
    print("Something we went wrong")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
