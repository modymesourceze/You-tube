from mody import Mody
import json
import youtube_search
import yt_dlp
from pySmartDL import SmartDL
from requests import Session
from datetime import datetime
from asyncio import sleep, create_task
from threading import Thread
import os
from telebot.types import *

tkn = Mody.ELHYBA

bot = telebot.TeleBot(tkn)



user_is_search_youtube = "" # لا تعدلهن
search_word = "" # لا تعدلهن

@bot.message_handler(content_types=['text'])
def Yout(message: Message):
    global user_is_search_youtube, search_word
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        (msg_text.startswith("بحث") or msg_text.startswith("يوت") or msg_text.startswith("يوتيوب") )
        and len(message.text.split(" ")) > 1

    ):
            bot.send_chat_action(chat_id, "typing")
            user_is_search_youtube = user_.id
            search_word = " ".join(message.text.split(" ")[1:])
            bot.send_message(message.chat.id, text='هذة عمليآت آلنآتجة من آلبحٿ آنقر على آلفيديو آلذي تريد تحملية 😁 !' , reply_markup=MrkSr(search_word), reply_to_message_id=message.id)
            bot.delete_message(chat_id, message.id)

    else:
        bot.send_message(message.chat.id, text="للبحث اكتب (بحث او يوت او يوتيوب) ثم كلمه البحث", reply_to_message_id=message.id)

            
from pytube import YouTube, Search
def SendOpSr(srWod:str):
    yt = Search(srWod)

    ur = yt.results
    urls = []
    a = 0
    for i in ur:
        if a == 5:
            break
        i = str(i)
        urs = i[i.find("videoId"): i.find(">")].replace("videoId=", "")
        urls.append("https://www.youtube.com/watch?v=" +urs)
        a += 1
    b = 0
    liul = []
    while b < len(urls) :
        sr =YouTube(urls[b])
        tit = sr.title
        liul.append([tit, urls[b]])
        b += 1
    return liul


def MrkSr(word):
    global sors
    mrk = InlineKeyboardMarkup(row_width=1)
    btns = []
    sors = []
    b = 0
    for ur in SendOpSr(word):
        print(ur[0])
        btn = InlineKeyboardButton(text=ur[0], callback_data=ur[1])
        btns.append(btn)
        sors.append(ur[1])
        b += 1
    mrk.add(*btns)
    
    return mrk

def MrkSr(word):
    global sors
    mrk = InlineKeyboardMarkup(row_width=1)
    btns = []
    sors = []
    b = 0
    for ur in SendOpSr(word):
        print(ur[0])
        btn = InlineKeyboardButton(text=ur[0], callback_data=ur[1])
        btns.append(btn)
        sors.append(ur[1])
        b += 1
    mrk.add(*btns)
    
    return mrk

@bot.callback_query_handler(func= lambda call:True)
def QueryYoutube(call:CallbackQuery):
    chid = call.message.chat.id
    data = call.data
    message = call.message
    user = call.from_user
    if "https://www.youtube.com/watch?v=" in data:
        # bot.send_chat_action(chid, action="sending audio")
        if user_is_search_youtube == user.id:
            yt = YouTube(data)
            bot.delete_message(message.chat.id, message.id)
            yt.streams.get_audio_only().download(filename=search_word + '.wav')
 
            bot.send_audio(message.chat.id, open(search_word + '.wav', 'rb'), caption=yt.title,  parse_mode="HTML")
            os.remove(search_word + '.wav')


bot.infinity_polling(skip_pending=True)