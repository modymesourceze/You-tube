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
import telebot
from pytube import YouTube
import random
from telebot import types
#@elhyba
#المطور
tkn = Mody.TG_BOT_TOKEN
bot = telebot.TeleBot(tkn)
#@elhyba
print(' Go Bot /Start ')
@bot.message_handler(commands=['start'])
def message1(message):
    id1 = str(message.from_user.id)
    #@elhyba
    #@elhyba


    
    ty = types.InlineKeyboardButton(text='دخول البوت',callback_data='ty')
    kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
    bot.send_message(message.chat.id,'*اهلا بك في بوت تحميل من اليوتيوب*',parse_mode='markdown',reply_markup=kj)

@bot.callback_query_handler(func=lambda call:True)
def call(call):
    if call.data =='ty':
        nc = types.InlineKeyboardButton(text='تحميل فيديو',callback_data='nc')
        cn = types.InlineKeyboardButton(text='تحميل مقطع صوتي',callback_data='cn')
        ncc = types.InlineKeyboardMarkup(row_width=1)
        ncc.add(nc,cn)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*اختار التحميل المناسب*',reply_markup=ncc,parse_mode='markdown')
    elif call.data =='nc':
        mk = types.InlineKeyboardButton(text='قناة مطور لبوت',url='https://t.me/Source_Ze')
        mk1 = types.InlineKeyboardMarkup(row_width=1)
        mk1.add(mk)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*ارسل الان رابط المقطع من فضلك*',reply_markup=mk1,parse_mode='markdown')
        bot.register_next_step_handler(message,m1,message.id)
    elif call.data =='cn':
        mk = types.InlineKeyboardButton(text='قناة البوت',url='https://t.me/Source_Ze')
        mk1 = types.InlineKeyboardMarkup(row_width=1)
        mk1.add(mk)
        message = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='*ارسل الان رابط المقطع من فضلك*',reply_markup=mk1,parse_mode='markdown')
        bot.register_next_step_handler(message,m2,message.id)
    #@elhyba
    #@elhyba
def m1(message,id):
    id1 = str(message.from_user.id)
    me = str(message.text)
    if ('https') in me :
        #@elhyba
        #@elhyba
        ty = types.InlineKeyboardButton(text='مبرمج البوت',url='https://t.me/elhyba')
        kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*جار التحميل الان..*',reply_markup=kj,parse_mode='markdown')
        video_url = me
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download()
        #@elhyba

    
        filem = video.default_filename
     
        ki='qwertyuioplkjhgfdsazxcvbn'
        uo = str(''.join(random.choice(ki)for ii in range(4)))
        #@elhyba
       
        namenew = f'{uo}.mp4'
        os.rename(filem, namenew)
        bot.send_video(id1,video=open(f'{uo}.mp4','rb'),caption='*تم التحميل بنجاح*',parse_mode='markdown',reply_markup=kj)
        os.remove(filem)
        os.remove(f'{uo}.mp4')
 #@elhyba       
    else:
        mi = types.InlineKeyboardButton(text='القائمة الرئسية',callback_data='ty')
        mi1 = types.InlineKeyboardMarkup(row_width=2);mi1.add(mi)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*عذرا ارسل رابط صحيح من فضلك*',parse_mode='markdown',reply_markup=mi1)
def m2(message,id):
    id1 = str(message.from_user.id)
    me = str(message.text)
    if ('https') in me :
        ty = types.InlineKeyboardButton(text='مبرمج البوت',url='https://t.me/elhyba')
        kj = types.InlineKeyboardMarkup(keyboard=[[ty]])
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*جار التحميل الان..*',reply_markup=kj,parse_mode='markdown')
        video_url = me
        yt = YouTube(video_url)
        video = yt.streams.first()
        video.download()
#@elhyba
    
        filem = video.default_filename
     
        u='qwertyuioplkjhgfdsazxcvbn'
        rr = str(''.join(random.choice(u)for ii in range(4)))
        namenew = f'{rr}.mp4'
        os.rename(filem, namenew)
        with open(namenew,'rb') as ad:
            bot.send_audio(id1,ad,caption='*تم التحميل بنجاح*',parse_mode='markdown')
            os.remove(filem)
            os.remove(f'{rr}.mp3')   
            #@elhyba 
    else:
        mi = types.InlineKeyboardButton(text='القائمة الرئسية',callback_data='ty')
        mi1 = types.InlineKeyboardMarkup(row_width=2);mi1.add(mi)
        bot.edit_message_text(chat_id=message.chat.id,message_id=id,text='*عذرا ارسل رابط صحيح من فضلك*',parse_mode='markdown',reply_markup=mi1)
#@elhyba



#@elhyba
def main():
    #@elhyba  
    while True:
        
        try:
            
            bot.polling()
            
        except:
            import os
            os.system('clear')
#@elhyba
            main()
        
        main()
        
    main()
    
main()


#حقوق @elhyba تخمط اضحك  فضيحه صبر شريف وخلي يوزر لمطور
#@elhyba
