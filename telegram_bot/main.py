from telebot import TeleBot
from telebot.types import (InputMediaPhoto,
                           InputMediaVideo,
                           InputMediaAudio,
                           InputMediaDocument,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           KeyboardButton,
                           ReplyKeyboardMarkup, )
from database import (get_all,
                      get_by_id,
                      DB_CONNECTION,
                      GET_ALL_USERS,
                      GET_SCH_BY_USER_ID_NOT_SENT,
                      GET_CHAT_BY_USER_ID,
                      GET_BOT_BY_USER_ID,
                      GET_POST_BY_ID,
                      GET_TEMPLATE_BY_ID,
                      UPDATE_SCHED_SET_SENT,
                      update)
from datetime import datetime
from time import sleep
from os import path

MEDIA_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "\\core\\static\\media" + "\\"
hr = '_______________________________\n'


def auto_post():
    # получить всех юзеров
    users = get_all(DB_CONNECTION, GET_ALL_USERS)
    for user in users:
        user_id = user[0]
        # print(user)

        # цикл - получить расписание неотправленных постов с каждым юзером
        schedule = get_by_id(DB_CONNECTION, GET_SCH_BY_USER_ID_NOT_SENT, (user_id, False))
        for sched in schedule:
            sched_datetime = datetime.strptime(sched[0], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M')
            post_id = sched[1]
            sched_id = sched[3]
            datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M')
            # print(sched)

            # Проверка по дате-времени, если совпадает, то continue
            if datetime_now == sched_datetime:
                print('OK!')

                # цикл - по чатам с user_id
                chats = get_by_id(DB_CONNECTION, GET_CHAT_BY_USER_ID, (user_id,))
                for chat in chats:
                    chat_username = chat[0].split('/')[-1]
                    print(chat_username)

                    # Цикл по ботам с user_id
                    bots = get_by_id(DB_CONNECTION, GET_BOT_BY_USER_ID, (user_id,))
                    for bot in bots:
                        bot_token = bot[0]

                        # цикл по постам c user_id
                        post = get_by_id(DB_CONNECTION, GET_POST_BY_ID, (post_id,))[0]
                        print(post)
                        text = post[0]
                        template_id = post[13]
                        template = get_by_id(DB_CONNECTION, GET_TEMPLATE_BY_ID, (template_id,))[0][3].replace('<p>', '').replace('</p>', '')
                        text = text + hr + template

                        photo_list = []
                        if post[1]: photo_list.append(post[1])
                        if post[2]: photo_list.append(post[2])
                        if post[3]: photo_list.append(post[3])
                        if post[4]: photo_list.append(post[4])
                        if post[5]: photo_list.append(post[5])
                        print(photo_list)
                        url_btn = []
                        if post[6]: url_btn.append(post[6])
                        if post[7]: url_btn.append(post[7])

                        video = ''
                        if video: MEDIA_DIR + post[8]

                        # Todo add music and document

                        markup = InlineKeyboardMarkup()
                        if url_btn:
                            markup.row_width = 2
                            markup.add(
                                InlineKeyboardButton(text=url_btn[1], url=url_btn[0], callback_data="...")
                                )
                        btn_list = []
                        if post[9]: btn_list.append(post[9])
                        if post[10]: btn_list.append(post[10])
                        if post[11]: btn_list.append(post[11])
                        if post[12]: btn_list.append(post[12])

                        # Todo handle btn count
                        if btn_list:
                            if len(btn_list) == 1:
                                markup.add(InlineKeyboardButton(text=btn_list[0], callback_data="...", ))
                            if len(btn_list) == 2:
                                markup.add(
                                    InlineKeyboardButton(text=btn_list[0], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[1], callback_data="...", ),
                                )
                            if len(btn_list) == 3:
                                markup.add(
                                    InlineKeyboardButton(text=btn_list[0], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[1], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[2], callback_data="...", ),
                                )
                            if len(btn_list) == 4:
                                markup.add(
                                    InlineKeyboardButton(text=btn_list[0], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[1], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[2], callback_data="...", ),
                                    InlineKeyboardButton(text=btn_list[3], callback_data="...", ),
                                )

                        bot = TeleBot(bot_token)

                        # Отправить сообщение только текст
                        if not photo_list and not video:
                            bot.send_message(chat_id='@' + chat_username, text=text, reply_markup=markup)
                            update(DB_CONNECTION, UPDATE_SCHED_SET_SENT, (True, sched_id))
                        elif photo_list and not video:
                            if len(photo_list) == 1:
                                bot.send_photo(chat_id='@' + chat_username, photo=open(MEDIA_DIR + photo_list[0], 'rb'), caption=text, parse_mode='HTML', reply_markup=markup)
                            elif len(photo_list) == 2:
                                bot.send_media_group(chat_id='@' + chat_username, media=[
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[0], 'rb'), caption=text, parse_mode='HTML'),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[1], 'rb')),
                                ])
                            elif len(photo_list) == 3:
                                bot.send_media_group(chat_id='@' + chat_username, media=[
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[0], 'rb'), caption=text, parse_mode='HTML'),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[1], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[2], 'rb')),

                                ])
                            elif len(photo_list) == 4:
                                bot.send_media_group(chat_id='@' + chat_username, media=[
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[0], 'rb'), caption=text, parse_mode='HTML'),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[1], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[2], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[3], 'rb')),

                                ])
                            elif len(photo_list) == 5:
                                bot.send_media_group(chat_id='@' + chat_username, media=[
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[0], 'rb'), caption=text, parse_mode='HTML'),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[1], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[2], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[3], 'rb')),
                                    InputMediaPhoto(media=open(MEDIA_DIR + photo_list[4], 'rb')),
                                ])
                            update(DB_CONNECTION, UPDATE_SCHED_SET_SENT, (True, sched_id))

                        elif video and not photo_list:
                            bot.send_video(chat_id='@' + chat_username, video=open(MEDIA_DIR + video, 'rb'),
                                           caption=text, parse_mode='HTML', reply_markup=markup)
                            update(DB_CONNECTION, UPDATE_SCHED_SET_SENT, (True, sched_id))


while True:
    auto_post()
    sleep(1)
