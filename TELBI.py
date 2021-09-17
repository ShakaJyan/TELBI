
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)
import telebot # pip install pyTelegramBotAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import time
from PIL import Image
import schedule   #pip install schedule
import threading
import random
from gtts import gTTS #pip install gTTS
import pyautogui as pag  #pip install pyautogui
import pywinauto    #pip install pywinauto
import pygetwindow as gw

#음식 패키지
from package import koreafood_package, japanfood_package, usafood_package, chinafood_package

#운동 패키지
from package import cardio_package, weight_package

#음식 사진 저장 및 경로 검색
from package import getphoto_package, pathsearch

#뉴스 패키지
from package import corona_package,headline_package,politics_package,economy_package,social_package

#날씨 패키지
from package import weather_package

#텍스트 음성 변환 및 자동 클릭 패키지
from package import tts_package,click_package

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
now = time.localtime()
chat_id = 

opts = webdriver.ChromeOptions()
opts.add_argument('window-size=960,750')

now = time.localtime(time.time())
hour = now.tm_hour

CATEGORY = range(1)

EXERCISE,MEAL,NEWS,WEATHER,CARDIOEXERCISE,WEIGHTTRAINING,KOREA,JAPAN,USA,CHINA,CORONA,HEADLINE,POLITICS,ECONOMY,SOCIAL = range(15)

# 시작 
def start(update:Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s  started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("1.운동", callback_data=str(EXERCISE)),
            InlineKeyboardButton("2.식사", callback_data=str(MEAL)),
            InlineKeyboardButton("3.뉴스", callback_data=str(NEWS)),
            InlineKeyboardButton("4.날씨", callback_data=str(WEATHER)),
            
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "안녕하세요 텔비입니다." + "원하시는걸 선택해주세요!", reply_markup=reply_markup
        )
    return CATEGORY

# 운동
def exercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("유산소 운동", callback_data=str(CARDIOEXERCISE)),
            InlineKeyboardButton("웨이트 트레이닝", callback_data=str(WEIGHTTRAINING)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="어떤 운동 하시겠어요?", reply_markup=reply_markup)
    return CATEGORY

def cardioexercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="유산소 운동을 추천해드릴게요.")
    x = cardio_package.cardio_pack(bot, chat_id)   
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

    return ConversationHandler.END

def weighttraining(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="웨이트 트레이닝을 추천해드릴게요.")
    x = weight_package.weight_pack(bot,chat_id)    
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    
    return ConversationHandler.END

# 식사
def meal(update:Update,_: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("한식", callback_data=str(KOREA)),
            InlineKeyboardButton("일식", callback_data=str(JAPAN)),
            InlineKeyboardButton("양식", callback_data=str(USA)),
            InlineKeyboardButton("중식", callback_data=str(CHINA)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="음식 메뉴를 선택해주세요!", reply_markup=reply_markup)
    return CATEGORY

def korea(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="한식을 선택하셨습니다!")
    result = koreafood_package.koreafood(bot, chat_id)
    getphoto_package.getphoto(result, bot, chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def japan(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="일식을 선택하셨습니다!")
    result = japanfood_package.japanfood(bot, chat_id)
    getphoto_package.getphoto(result,bot,chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def usa(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="양식을 선택하셨습니다!")
    result = usafood_package.usafood(bot, chat_id)
    getphoto_package.getphoto(result,bot,chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END
    
def china(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="중식을 선택하셨습니다.")
    result = chinafood_package.chinafood(bot, chat_id)
    getphoto_package.getphoto(result,bot,chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

    return ConversationHandler.END

# 뉴스
def news(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("코로나", callback_data=str(CORONA)),
            InlineKeyboardButton("헤드라인", callback_data=str(HEADLINE)),
            InlineKeyboardButton("정치", callback_data=str(POLITICS)),
            InlineKeyboardButton("경제", callback_data=str(ECONOMY)),
            InlineKeyboardButton("사회", callback_data=str(SOCIAL)),

            

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="카테고리를 선택해주세요", reply_markup=reply_markup)
    return CATEGORY

def corona(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="코로나 현황을 선택하셨습니다.")
    x = corona_package.corona_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def headline(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="헤드라인 뉴스를 선택하셨습니다.")
    x = headline_package.headline_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def politics(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="정치뉴스를 선택하셨습니다.")
    x = politics_package.politics_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def economy(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="경제뉴스를 선택하셨습니다.")
    x = economy_package.economy_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

def social(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="사회뉴스를 선택하셨습니다.")
    x = social_package.social_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

# 날씨
def weather(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="날씨를 선택하셨습니다.")
    x = weather_package.weather(bot,chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    return ConversationHandler.END

#대화 형식으로 이어질수 있게 conversation 핸들러로 묶었습니다.
def main() -> None:
    updater = Updater("1709776665:AAF-sEQXF2TAW67-aOno7o4zrDoiGSeeRrU")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            CATEGORY: [
                CallbackQueryHandler(exercise, pattern='^' + str(EXERCISE) + '$'),
                CallbackQueryHandler(cardioexercise, pattern='^' + str(CARDIOEXERCISE) + '$'),
                CallbackQueryHandler(weighttraining, pattern='^' + str(WEIGHTTRAINING) + '$'),
                CallbackQueryHandler(news, pattern='^' + str(NEWS) + '$'),
                CallbackQueryHandler(corona, pattern='^' + str(CORONA) + '$'),
                CallbackQueryHandler(headline, pattern='^' + str(HEADLINE) + '$'),
                CallbackQueryHandler(politics, pattern='^' + str(POLITICS) + '$'),
                CallbackQueryHandler(economy, pattern='^' + str(ECONOMY) + '$'),
                CallbackQueryHandler(social, pattern='^' + str(SOCIAL) + '$'),
                CallbackQueryHandler(weather, pattern='^' + str(WEATHER) + '$'),
                CallbackQueryHandler(meal, pattern='^' + str(MEAL) + '$'),
                CallbackQueryHandler(korea, pattern='^' + str(KOREA) + '$'),
                CallbackQueryHandler(japan, pattern='^' + str(JAPAN) + '$'),
                CallbackQueryHandler(usa, pattern='^' + str(USA) + '$'),
                CallbackQueryHandler(china, pattern='^' + str(CHINA) + '$'),
                
            ],
        },
        fallbacks= [CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()

# 스케줄화
def wakeup_time():
    bot.send_message(chat_id, "굿모닝 좋은 아침입니다! ")
    x = weather_package.weather(bot,chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def morning_corona():
    bot.send_message(chat_id, "코로나 현황에 대해 알려드릴게요.")
    x = corona_package.corona_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def breakfast_time():
    bot.send_message(chat_id, "아침 메뉴 한식 추천드릴게용")
    result = koreafood_package.koreafood(bot, chat_id)
    getphoto_package.getphoto(result, bot, chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def morning_headline():
    bot.send_message(chat_id, "아침 헤드라인 뉴스 들려드릴게요~")
    x = headline_package.headline_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    
def Break_time():
    if hour >= 9 and hour < 13:
        bot.send_message(chat_id, f"주인님 현재 {now.tm_hour}시{now.tm_min}분 입니다."
                +"\n쉬는시간입니다. 다음 시간을 위해 충분히 쉬어주세요.")
    elif hour >= 23 and hour < 24:
        bot.send_message(chat_id, f"주인님 현재 {now.tm_hour}시{now.tm_min}분 입니다."
                +"\n쉬는시간입니다. 다음 시간을 위해 충분히 쉬어주세요.")
    else:
        return  
    
def launch_time():
    bot.send_message(chat_id, "점심 메뉴 중식 추천드릴게요")
    result = chinafood_package.chinafood(bot, chat_id)
    getphoto_package.getphoto(result,bot,chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def launch_news():
    bot.send_message(chat_id ,"사회 뉴스 알려드릴게용")
    x = social_package.social_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def gym_time():
    bot.send_message(chat_id ,"오늘 웨이트 운동 추천 드릴게요!")
    x = weight_package.weight_pack(bot,chat_id) 
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

    return ConversationHandler.END

def dinner_news():
    bot.send_message(chat_id, "오늘 경제 뉴스 알려 드릴게요!")
    x = economy_package.economy_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    
def dinner_time():
    bot.send_message(chat_id, "저녁 양식메뉴 추천드릴게요~")
    result = usafood_package.usafood(bot, chat_id)
    getphoto_package.getphoto(result,bot,chat_id)
    x = pathsearch.path(result,bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()

def night_news():
    bot.send_message(chat_id, "오늘 핫한 정치뉴스 들려드릴게요")
    x = politics_package.politics_pack(bot, chat_id)
    tts_package.tts(x,bot,chat_id)
    time.sleep(0.5)
    click_package.click()
    
def sleep_time():
    bot.send_message(chat_id, "주무실 시간입니다. 좋은 밤되세요!")

schedule.every().day.at("23:52").do(wakeup_time)
schedule.every().day.at("23:53").do(morning_corona)
schedule.every().day.at("23:54").do(breakfast_time)
schedule.every().day.at("23:55").do(morning_headline)
schedule.every().day.at("23:56").do(launch_time)
schedule.every(3).minutes.do(Break_time)
schedule.every().day.at("00:02").do(gym_time)
schedule.every().day.at("00:03").do(dinner_news)
schedule.every().day.at("00:04").do(dinner_time)
schedule.every().day.at("00:05").do(night_news)
schedule.every().day.at("00:06").do(sleep_time)

def AutoThread1(name):
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
t1 = threading.Thread(target=AutoThread1, args=('1'))
t1.start()

if __name__ == '__main__':
    main()
