import praw
import os
import requests
import io
import imghdr
import telegram
import re
import telebot
#import telegram_send
from PIL import Image
from io import BytesIO
import moviepy
import random
import time
from moviepy.editor import *
from telegram import Bot, InputFile
from numpy import inf
from moviepy.editor import VideoFileClip
import subprocess
import json
from moviepy.editor import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, PreCheckoutQueryHandler, InlineQueryHandler, MessageHandler, Filters
from dotenv import load_dotenv
import telegram.ext
from telegram.error import TelegramError
import stripe
from telebot.types import LabeledPrice
import mariadb
from mariadb import Error
from datetime import date
import threading
from telegram import ChatAction, Update, Bot
import openai
import os


#DON'T START THE SERVER WITHOUT STARTING MARIADB SERVER OR PAYMENTS WON'T BE REGISTERED!!!!!!!!!!!!!!

active_users = []


# Set your API key
stripe.api_key = "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"




#BOT_TOKEN = '5861175915:AAG0qb_-osHcHILKMhWuPunM2I8PrVNkfik'
BOT_TOKEN = '5833460127:AAG2pu8DHDmDpOn9Z0PoRHV2iAkDAb3E2Ns'
sentmess = 0
sentmess2 = sentmess
bot = telebot.TeleBot(BOT_TOKEN)
from telegram import InputMediaPhoto
global xchatid
xchatid = 5362284509
global freecount
freecount = 0
global paiduser
paiduser = False
# Initialize a Reddit instance
reddit = praw.Reddit(
    client_id="Gou7gDR-fuRj-JHm6Ey_9w",
    client_secret="db18CbyaTSa-GtT-ltiIeL1J6LxUlw",
    username="net777infamous",
    password="drahciR0nline",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
)
openai.api_key = "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"
# Specify the subreddit you want to get posts from

# Define the function that will handle the start command




# Iterate over the posts
# for post in new_posts:
   # print(post.title) # Print the title of each post
#start_button = InlineKeyboardButton("⬇️⬇️⬇️", callback_data="/start")
global button_clicked
button_clicked = {}
global subreddits_list
subreddits_list = []
subreddits_list = ['upskirt', 'pussy', 'HappyEmbarrassedGirls', 'TwerkQueens', 'AsianNSFW', 'BubbleButts', 'Ebony', 'FlashingAndFlaunting', 'PussyFlashing', 'SschoolGirlSkirts', 'DressedAndUndressed', 'PantiesToTheSide', 'paag', 'pawg', 'petite', 'Phatasswhitegirls', 'RedheadGifs', 'vagina', '18_19', 'FertileGirls', 'PLASTT', 'booty', 'boobs', 'sxygirlsinjeans', 'LegalTeens', 'bigasses', 'CamSluts', 'tiktokporn', 'collegesluts', 'hugeboobs']

start_button = [[InlineKeyboardButton("photo", callback_data='/sendjpg'),
                         InlineKeyboardButton("video", callback_data='/sendgif')],
                        [InlineKeyboardButton("", callback_data='3')]]

inline_keyboard = json.dumps(InlineKeyboardMarkup(start_button).to_dict())
                # Define the start command handler


                # Create an updater and dispatcher for the bot
#updater = Updater('5861175915:AAG0qb_-osHcHILKMhWuPunM2I8PrVNkfik')
updater = Updater(BOT_TOKEN)

                



                # Start polling for updates
global last_command_time
last_command_time = None 
global startcheck
startcheck = False
updater.stop()

# Wait for a few seconds to make sure the bot is stopped


updater.start_polling()
dispatcher = updater.dispatcher  
#@bot.message_handler(commands=['start', 'hello'])
@bot.message_handler(commands=['sendgif'])
@bot.message_handler(commands=['sendjpg'])
@bot.message_handler(commands=['starty'])

def print_numbers():
    for i in range(1, 11):
        print(i)


def print_numbers2():
    for i in range(1, 11):
        print(i)


def print_numbers3(xchatid):
    for i in range(1, 11):
        print(i + xchatid)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers2)
thread3 = threading.Thread(target=print_numbers3)

def handle_message(update, context):
    # Get the user's message
   
    message_text = update.message.text
    print(message_text)
    if message_text == "send nudes":
          sendjpg_command
          
    if message_text == "/start":
            global startcheck
            global xchatid
            xchatid = update.message.chat_id
            global subreddits_list
            print ("chat_id = "+ str(xchatid))
            if xchatid == 5362284509:
                subreddits_list = ['upskirt', 'pussy', 'HappyEmbarrassedGirls', 'TwerkQueens', 'AsianNSFW', 'BubbleButts', 'Ebony', 'FlashingAndFlaunting', 'PussyFlashing', 'SschoolGirlSkirts', 'DressedAndUndressed', 'PantiesToTheSide', 'paag', 'pawg', 'petite', 'Phatasswhitegirls', 'RedheadGifs', 'vagina', '18_19', 'FertileGirls', 'PLASTT', 'booty', 'boobs', 'sxygirlsinjeans', 'LegalTeens', 'bigasses', 'CamSluts', 'tiktokporn', 'collegesluts', 'hugeboobs']
            else:
                subreddits_list = [ 'memes', 'blackpeopletwitter', 'funny', 'meirl', 'meme', 'pics','shitposting','mademesmile','unexpected', 'murderedbywords', 'tinder', 'tumblr', 'whitepeopletwitter','aww','animalsbeingbros','wellthatsucks','nextfuckinglevel','kidsarefuckingstupid', 'publicfreakout', 'politicalhumor', 'antiwork'] 
            global paiduser
            global membername
            subreddit_name = random.choice(subreddits_list)
            # Get the subreddit instance
            subreddit = reddit.subreddit(subreddit_name)
        # total_members = bott.get_chat_member(xchatid, 5861175915) 
            
            total_members = bott.get_chat_member(xchatid, 5833460127) 
            print(f'Total members: {total_members}')
            first_name = total_members['user']['first_name']
            membername = first_name
            print(first_name)
        #  bot.send_chat_action(chat_id=xchatid, action=ChatAction.TYPING)
        #  time.sleep(2)
            help_command(update, context)
                        

            # Get new posts from the subreddit
            new_posts = subreddit.random() # Limit to 
            photo_path = '/home/richa/Downloads/shrek.jpg'
            try:
                       print("launching") 
                        

                        # Add the command and callback query handlers

                        
                        #bot.send_photo(chat_id=xchatid, photo=open(photo_path, 'rb'), reply_markup=inline_keyboard)
                        #bot.send_message(chat_id=xchatid, text ="" , reply_markup=inline_keyboard)
                        #print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                            #  bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_PHOTO)
                                #time.sleep(5) 
                            
                    
            except Exception as e: print(e)
            try:
                    conn = mariadb.connect(
                        user="richa",
                        password="opop",
                        host="192.168.8.114",
                        port=3306,
                        database="telebot"
                    )
                    print("Connection successful!")
            
                    # Create a cursor object
                    cur = conn.cursor()

                    # Define the SQL query to select data from the 'users' table
                    query = "SELECT COUNT(*) FROM telebot.users WHERE id = '" + str(xchatid) + "'"

                    # Execute the query
                    cur.execute(query)

                    # Fetch the result
                    result = cur.fetchone()[0]

                    # If the value exists, do something
                    if result > 0:
                        print("Premium user joined")
                        paiduser = True
                        # Your code or action here
                    else:
                        print("Normie user joined")
                        paiduser = False

                    # Close the cursor and connection
                    cur.close()
                    conn.close()
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")                 
                # Commit the changes to the database
    else:     

    # Use the ChatGPT API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message_text,
            frequency_penalty = 1.0,
            presence_penalty = 1.0,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1.0,
        )
        # Get the generated response from the API and send it to the user
        bot.send_chat_action(chat_id=xchatid, action=ChatAction.TYPING)
        time.sleep(2)
        bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text, reply_markup=inline_keyboard)

    
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


def start_command(update, context):
    global startcheck
    global xchatid
    xchatid = update.message.chat_id
    '''
    if xchatid in active_users:
           #do nothing
    else:
        #add them to list of users
        active_users.append(xchatid)
        #create subreddit list for them
        subreddits_list = ['upskirt', 'pussy', 'HappyEmbarrassedGirls', 'TwerkQueens', 'AsianNSFW', 'BubbleButts', 'Ebony', 'FlashingAndFlaunting', 'PussyFlashing', 'SschoolGirlSkirts', 'DressedAndUndressed', 'PantiesToTheSide', 'paag', 'pawg', 'petite', 'Phatasswhitegirls', 'RedheadGifs', 'vagina', '18_19', 'FertileGirls', 'PLASTT', 'booty', 'boobs', 'sxygirlsinjeans', 'LegalTeens', 'bigasses', 'CamSluts', 'tiktokporn', 'collegesluts', 'hugeboobs']
        #check if they are a paid user
        
        '''
    global subreddits_list
    print ("chat_id = "+ str(xchatid))
    if xchatid == 5362284509:
        subreddits_list = ['upskirt', 'pussy', 'HappyEmbarrassedGirls', 'TwerkQueens', 'AsianNSFW', 'BubbleButts', 'Ebony', 'FlashingAndFlaunting', 'PussyFlashing', 'SschoolGirlSkirts', 'DressedAndUndressed', 'PantiesToTheSide', 'paag', 'pawg', 'petite', 'Phatasswhitegirls', 'RedheadGifs', 'vagina', '18_19', 'FertileGirls', 'PLASTT', 'booty', 'boobs', 'sxygirlsinjeans', 'LegalTeens', 'bigasses', 'CamSluts', 'tiktokporn', 'collegesluts', 'hugeboobs']
    else:
        subreddits_list = [ 'memes', 'blackpeopletwitter', 'funny', 'meirl', 'meme', 'pics','shitposting','mademesmile','unexpected', 'murderedbywords', 'tinder', 'tumblr', 'whitepeopletwitter','aww','animalsbeingbros','wellthatsucks','nextfuckinglevel','kidsarefuckingstupid', 'publicfreakout', 'politicalhumor', 'antiwork'] 
    global paiduser
    global membername
    subreddit_name = random.choice(subreddits_list)
    # Get the subreddit instance
    subreddit = reddit.subreddit(subreddit_name)
   # total_members = bott.get_chat_member(xchatid, 5861175915) 
    
    total_members = bott.get_chat_member(xchatid, 5833460127) 
    print(f'Total members: {total_members}')
    first_name = total_members['user']['first_name']
    membername = first_name
    print(first_name)
  #  bot.send_chat_action(chat_id=xchatid, action=ChatAction.TYPING)
  #  time.sleep(2)
    help_command(update, context)
                

    # Get new posts from the subreddit
    new_posts = subreddit.random() # Limit to 
    photo_path = '/home/richa/Downloads/shrek.jpg'
    try:
                
                

                # Add the command and callback query handlers
                '''
                
                print(new_posts.url)
                if new_posts.url.endswith('.gif'):
                        try:
                            response = requests.get(new_posts.url)
                            
                            if response.status_code == 200:
                                video_bytes = BytesIO(response.content)
                                video_bytes.name = new_posts.title + '.gif'
                                upvotes = new_posts.score
                                comments = new_posts.num_comments
                                print(upvotes)
                                bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                bot.send_video(chat_id=5362284509, video=video_bytes, caption='['+subreddit_name+']  '+video_bytes.name+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                                time.sleep(2)
                                print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                                print("hshsh   "+update.callback_query.id)
                                #bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                #time.sleep(10)
                        
                        except Exception as e: print(e)

                if new_posts.url.endswith('.gifv'):
                    try:
                        old_url = new_posts.url
                        new_url = old_url.replace(".gifv", ".mp4")
                        response = requests.get(new_url)
                        
                        if response.status_code == 200:
                                video_bytes = BytesIO(response.content)
                                video_bytes.name = new_posts.title + '.mp4'
                                print(video_bytes.name)
                                upvotes = new_posts.score
                                comments = new_posts.num_comments
                                print(upvotes)
                                bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                bot.send_video(chat_id=5362284509, video=video_bytes, caption='['+subreddit_name+']  '+video_bytes.name+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                                print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                                time.sleep(2)
                              #  bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                #time.sleep(10)
                    except Exception as e: print(e)
                   # continue
                   '''

                
                bot.send_photo(chat_id=xchatid, photo=open(photo_path, 'rb'), reply_markup=inline_keyboard)
                #bot.send_message(chat_id=xchatid, text ="" , reply_markup=inline_keyboard)
                #print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                      #  bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_PHOTO)
                        #time.sleep(5) 
                      
               
    except Exception as e: print(e)
    try:
            conn = mariadb.connect(
                user="richa",
                password="opop",
                host="192.168.8.114",
                port=3306,
                database="telebot"
            )
            print("Connection successful!")
    
            # Create a cursor object
            cur = conn.cursor()

            # Define the SQL query to select data from the 'users' table
            query = "SELECT COUNT(*) FROM telebot.users WHERE id = '" + str(xchatid) + "'"

            # Execute the query
            cur.execute(query)

            # Fetch the result
            result = cur.fetchone()[0]

            # If the value exists, do something
            if result > 0:
                print("Premium user joined")
                paiduser = True
                # Your code or action here
            else:
                print("Normie user joined")
                paiduser = False

            # Close the cursor and connection
            cur.close()
            conn.close()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")                 
                # Commit the changes to the database





def nsfwmode(update, context):
    global subreddits_list

    subreddits_list = ['upskirt', 'pussy', 'HappyEmbarrassedGirls', 'TwerkQueens', 'AsianNSFW', 'BubbleButts', 'Ebony', 'FlashingAndFlaunting', 'PussyFlashing', 'SschoolGirlSkirts', 'DressedAndUndressed', 'PantiesToTheSide', 'paag', 'pawg', 'petite', 'Phatasswhitegirls', 'RedheadGifs', 'vagina', '18_19', 'FertileGirls', 'PLASTT', 'booty', 'boobs', 'sxygirlsinjeans', 'LegalTeens', 'bigasses', 'CamSluts', 'tiktokporn', 'collegesluts', 'hugeboobs']
    bot.send_message(xchatid, text = "nsfw mode")
    print("nsfw enabled")

def normode(update, context):
    global xchatid
    global subreddits_list
    if xchatid == 5362284509:
        subreddits_list = ['memes', 'blackpeopletwitter', 'meirl', 'meme']
    else: 
        subreddits_list = ['memes', 'blackpeopletwitter', 'funny', 'meirl', 'meme', 'pics','shitposting','mademesmile','unexpected', 'murderedbywords', 'tinder', 'tumblr', 'whitepeopletwitter','aww','animalsbeingbros','wellthatsucks','nextfuckinglevel','kidsarefuckingstupid', 'publicfreakout', 'politicalhumor', 'antiwork']      

  #  subreddits_list = ['upskirt' 'memes', 'blackpeopletwitter', 'ifunny', 'meirl', 'meme']  
    bot.send_message(xchatid, text = "clean mode")
    print("normal enabled")

def help_command(update, context):
    #bot.send_message(chat_id=xchatid, text="Hii there. I'm designed to scrape feeds from popular subreddits. Available commands: '/start , /clean , /nsfw , /help'  Support: inkdino@yahoo.com  (SADELA INC.)  NOTE: Most videos known to work only in nsfwmode, but don't fret.. I'll do my best to fetch the best of the best posts Reddit has to offer. You have 10 free video clicks, then a one-time fee of 5 USD for unlimited access and to keep me running. Just hit 'photo' or 'video' and I'll do the rest.")
    bot.send_message(chat_id=xchatid, text="Available commands: '/start , /clean , /nsfw , /help'  Support: inkdino@yahoo.com  (SADELA INC.)", reply_markup=inline_keyboard)
   
def sendgif_command(update, context):
    #subreddits_list2 = ['videos', 'YouTube', 'Documentaries', 'ArtisanVideos', 'mealtimevideos', 'educationalvideos', 'funnyvideos', 'ShortVideos', 'TikTokCringe', 'youtubehaiku', 'gifs', 'oddlysatisfying', 'ContagiousLaughter', 'animalsbeingjerks', 'nextfuckinglevel', 'UnnecessaryCensorship', 'HadToHurt', 'youseeingthisshit', 'holdmyredbull', 'aww']

    timeout = 0
    global subreddits_list
    global last_command_time
    global freecount
    global paiduser
    query = update.callback_query
    print(str(freecount) +"  trials used")
    if freecount > 10 and paiduser == False:
            print("your trial ended please purchase")
            bot.send_invoice(chat_id=xchatid, title= "ALERT", currency="USD", invoice_payload="cc", description="trial ended", provider_token="350862534:LIVE:YTBjNGU4OWIyNGQ0", prices = [LabeledPrice(label='Working Time Machine', amount=100), LabeledPrice('Extra Fees', 0)])
            query.answer()
    if paiduser == True or freecount < 11:
            freecount += 1
            #paid
    
            if last_command_time is not None and time.time() - last_command_time < 1:
                print("cooldown")
                bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "kindly wait 2 seconds between requests")
                query.answer()
                return
            #button_clicked[update.callback_query.data] = True

            while True:
                        timeout += 1
                        try:
                            
                            print("sendgif")
                            print(str(timeout) + " tries")
                            subreddit_name = random.choice(subreddits_list)

                                # Get the subreddit instance
                            subreddit = reddit.subreddit(subreddit_name)

                                # Get new posts from the subreddit
                            new_posts = subreddit.random() # Limit to 
                            response = requests.get(new_posts.url)
                            print("sendgif2")
                            print (new_posts.url)
                            if timeout == 15:
                                        print("giving up")
                                        bot.send_message(chat_id=xchatid, text= "**timeout**")
                                        break
                            

                            # Add the command and callback query handlers
                            try:
                                   
                                #  if post.url.endswith('.gif'):
                                #  try:
                                    '''                               user_comment = list(new_posts.comments)
                                        valid_comments = [comment for comment in user_comment if not re.search("automoderator", comment.author.name, re.IGNORECASE)]
                                    if valid_comments:
                                        comment = random.choice(valid_comments)
                                        comment_text = comment.body
                                    else:
                                        comment_text = ""
                                        {comments}"+'  '+comment_text,
                                                '''
                                    if new_posts.url.endswith('.gif'):
                                            try:
                                                    print("sendgif3")
                                                    video_bytes = BytesIO(response.content)
                                                    video_bytes.name = new_posts.title + '.gif'
                                                    upvotes = new_posts.score
                                                    comments = new_posts.num_comments
                                                    user_comment = list(new_posts.comments)
                                                    valid_comments = [comment for comment in user_comment if comment.author is not None and not re.search("automoderator", comment.author.name, re.IGNORECASE)]
                                                    if valid_comments:  
                                                        comment = random.choice(valid_comments)
                                                        comment_text = comment.body
                                                        comment_author = comment.author.name + ': '
                                                    else:
                                                        comment_text = ""
                                                        comment_author = "" + ': '
                                                        

                                                    author = new_posts.author
                                                    karma = str(author.link_karma + author.comment_karma)
                                                    author = str(new_posts.author)
                                                    print(upvotes)
                                                    bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_VIDEO)
                                                    if len(comment_author) > 3:
                                                        bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +video_bytes.name+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}"+'  '+ "\n" +comment_author+ comment_text, reply_markup=inline_keyboard)
                                                    else:
                                                        bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +video_bytes.name+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)

                                                    time.sleep(2)
                                                    print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                                                    #bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                                    #time.sleep(10)
                                                    print("sendgif4")
                                                    last_command_time = time.time()
                                                    query.answer()
                                                    break
                                            except Exception as e:
                                                            print(e)
                                                            print("stopped due to error...")
                                                            bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "something went wrong")

                                                            query.answer()
                                                            break
                                    if timeout == 15:
                                        print("giving up")
                                        bot.send_message(chat_id=xchatid, text= "**timeout**")
                                        break

                                    elif new_posts.url.endswith('.gifv'):
                                            print("gifv")
                                            try:
                                        
                                                    old_url = new_posts.url
                                                    new_url = old_url.replace(".gifv", ".mp4")
                                                    response = requests.get(new_url)
                                                    author = new_posts.author
                                                    karma = str(author.link_karma + author.comment_karma)
                                                    author = str(new_posts.author)
                                                
                                                    video_bytes = BytesIO(response.content)
                                                    video_bytes.name = new_posts.title + '.mp4'
                                                    print(video_bytes.name)
                                                    upvotes = new_posts.score
                                                    comments = new_posts.num_comments
                                                    user_comment = list(new_posts.comments)
                                                    valid_comments = [comment for comment in user_comment if comment.author is not None and not re.search("automoderator", comment.author.name, re.IGNORECASE)]
                                                    if valid_comments:  
                                                        comment = random.choice(valid_comments)
                                                        comment_text = comment.body
                                                        comment_author = comment.author.name + ': '
                                                    else:
                                                        comment_text = ""
                                                        comment_author = "" + ': '
                                                    print(upvotes)
                                                    bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_VIDEO)
                                                    if len(comment_author) > 3:
                                                        bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +video_bytes.name+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}"+'  '+ "\n" +comment_author+comment_text, reply_markup=inline_keyboard)
                                                    else:
                                                        bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +video_bytes.name+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                                                         
                                                    print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = ""))
                                                    time.sleep(2)
                                                    print ("givvvv")
                                                    last_command_time = time.time()
                                                    query.answer()
                                                    print("end")
                                                    break
                                                    
                                                #  bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                                    #time.sleep(10)
                                            except Exception as e:
                                                            print(e)
                                                            print("stopped due to error...")
                                                            bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "something went wrong")
                                                            query.answer()
                                                            break
                            except AttributeError as e:
                                print(f"Caught AttributeError: {e}")  
                                print("minor error..skipping")             
                            #else: 
                        
                        except Exception as e:
                                                    print(e)
                                                  #  freecount -=1
                                                    break                     #  continue
global freecount2
freecount2 = 0
def emptyfunc():
    print("empty")   
               
def sendjpg_command(update, context):
    timeout = 0
    global freecount2
    global subreddits_list
    global last_command_time
    global xchatid
   # if update.callback_query.data in button_clicked:
       #     return
    query = update.callback_query
    

    if last_command_time is not None and time.time() - last_command_time < 1:
        #query.edit_message_text(text='You already requested a gif. Please wait for the current request to finish.')
      #  time.sleep(5)
      #  context.chat_data['jpg_clicked'] = False
        print ("cooldown")
        bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "kindly wait 2 seconds between requests")
        query.answer()
       # bot.send_message(chat_id='5362284509', text="wait "+str(int(time.time() - last_command_time -10))+ " ")
        return
    
  #  context.chat_data['jpg_clicked'] = True
    
    while True:
                    
            try:
                    print("sendjpg")
                    timeout +=1

                    subreddit_name = random.choice(subreddits_list)

                        # Get the subreddit instance
                    subreddit = reddit.subreddit(subreddit_name)

                        # Get new posts from the subreddit
                    new_posts = subreddit.random() # Limit to 
        
                    print("sendjpg2")
                    
                    

                    # Add the command and callback query handlers
                    
                    print(new_posts.url)
                  #  if post.url.endswith('.gif'):
                  #  try:
                    response = requests.get(new_posts.url)
                                
                    if new_posts.url.endswith('.jpg'):


                            try:
                                    response = requests.get(new_posts.url)
                                    img = Image.open(BytesIO(response.content))
                                    img.thumbnail((1024, 1024))
                                    output = BytesIO()
                                    upvotes = new_posts.score
                                    author = new_posts.author
                                    karma = str(author.link_karma + author.comment_karma)
                                    author = new_posts.author
                                    karma = str(author.link_karma + author.comment_karma)
                                    author = str(new_posts.author)
                                    comments = new_posts.num_comments
                                    user_comment = list(new_posts.comments)
                                    valid_comments = [comment for comment in user_comment if comment.author is not None and not re.search("automoderator", comment.author.name, re.IGNORECASE)]
                                    if valid_comments:  
                                        comment = random.choice(valid_comments)
                                        comment_text = comment.body
                                        comment_author = comment.author.name + ': '
                                    else:
                                        comment_text = ""
                                        comment_author = "" + ': '
                                    print(upvotes)
                                    pictitle = new_posts.title + '.jpg'
                                    img.save(output, format='JPEG')
                                    photo_data = output.getvalue()
                                    
                                    bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_PHOTO)
                                  #  button_clicked[update.callback_query.data] = True
                                    
                                    
                                    #bot.send_photo(chat_id=xchatid, photo=photo_data, caption='['+subreddit_name+'/'+author+']  '+pictitle+'     '+f"👍 {upvotes} 💬 {comments}"+'  '+comment_text, reply_markup=inline_keyboard, parse_mode=telegram.ParseMode.MARKDOWN)
                                    if len(comment_author) > 3:
                                        bot.send_photo(chat_id=xchatid, photo=photo_data, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +pictitle+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}"+'  '+ "\n" +comment_author+ comment_text, reply_markup=inline_keyboard)
                                    else:
                                        bot.send_photo(chat_id=xchatid, photo=photo_data, caption='['+subreddit_name+'/'+author+'/'+karma+']  '+ "\n" +pictitle+'     '+ "\n" +f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)

                                    #bot.send_photo(chat_id='5362284509', photo=photo_data, caption='['+subreddit_name+']  '+pictitle+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard, reply_to_message_id=query.message.message_id)
                                  #  sentmess += 1
                                    print(bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "", cache_time=0,))
                                    
                                    last_command_time = time.time()
                                    query.answer()
                                    #context.chat_data['jpg_clicked'] = True
                                    
                                    
                                    print("end")
                                           
                                    break

                            except Exception as e:
                                            print(e)
                                            if str(e) == "'NoneType' object has no attribute 'id'":
                                                print ("minor error")
                                                query.answer()
                                                break
                                            else:
                                                print("stopped due to error...")
                                                bot.answer_callback_query(update.callback_query.id, show_alert = False, text = "something went wrong")
                                                query.answer()
                                                break
                    if timeout == 15:
                                    bot.send_message(chat_id=xchatid, text= "**timeout**")
                                    break
                    #if response.status_code != 200:
                     #               print ("minor error.. skipping")
                      #              continue
                 #   else: 
                              #      continue
                            
            except Exception as e:
                    print(e)
                    
                    break
global membername  
membername = "placeholder"               
     #   except Exception as e: print(e)
    #def send_welcome(message):


        
   # context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This is a bot that fetches images from a subreddit using praw and telegrambot. Type /help to see the available commands.")
dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CallbackQueryHandler(start_command, pattern='/start'))
dispatcher.add_handler(CommandHandler("sendgif", sendgif_command))
dispatcher.add_handler(CallbackQueryHandler(sendgif_command, pattern='/sendgif'))
dispatcher.add_handler(CommandHandler("sendjpg", sendjpg_command))
dispatcher.add_handler(CallbackQueryHandler(sendjpg_command, pattern='/sendjpg'))
dispatcher.add_handler(CommandHandler("nsfw", nsfwmode))
dispatcher.add_handler(CallbackQueryHandler(nsfwmode, pattern='/nsfw'))
dispatcher.add_handler(CommandHandler("clean", normode))
dispatcher.add_handler(CallbackQueryHandler(normode, pattern='/clean'))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CallbackQueryHandler(help_command, pattern='/help'))
'''
for post in new_posts:
        if post.is_self == False and post.url.endswith('.jpg'):
            media = InputMediaPhoto(post.url)
            bot.send_photo(chat_id='your_chat_id', photo=media)
       # print(post.title) 
       # if not submission.is_self and submission.url.endswith(('.jpg', '.jpeg', '.png')):
           # image_url = submission.url
            #telegram_send.send(images=[os.path.basename(image_url)], caption=image_url)
        #bot.reply_to(message, submission.url)
        5362284509
        '''
    #while True:


     

#bot.answer_callback_query(update.callback_query.id)
bott = telegram.Bot(token=BOT_TOKEN) 

'''
try:
        
    
        freecount +=1
        print(freecount)
        subreddit_name = random.choice(subreddits_list)

    # Get the subreddit instance
        subreddit = reddit.subreddit(subreddit_name)

    # Get new posts from the subreddit
        new_posts = subreddit.random() # Limit to 10 posts
        # Send videos via Telegram Bot API
                
        for x in new_posts.url:     
                subreddit_name = random.choice(subreddits_list)

    # Get the subreddit instance
                subreddit = reddit.subreddit(subreddit_name)

    # Get new posts from the subreddit
                new_posts = subreddit.random() # Limit to 10 posts

                # Add the command and callback query handlers

                
                print(new_posts.url)
                if new_posts.url.endswith('.gif'):
                        try:
                            response = requests.get(new_posts.url)
                            
                            if response.status_code == 200:
                                video_bytes = BytesIO(response.content)
                                video_bytes.name = new_posts.title + '.gif'
                                upvotes = new_posts.score
                                comments = new_posts.num_comments
                                print(upvotes)
                                bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_VIDEO)
                                bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+']  '+video_bytes.name+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                                time.sleep(2)
                            #    bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                break
                        
                        except Exception as e: print(e)

                if new_posts.url.endswith('.gifv'):
                    try:
                        old_url = new_posts.url
                        new_url = old_url.replace(".gifv", ".mp4")
                        response = requests.get(new_url)
                        
                        if response.status_code == 200:
                                video_bytes = BytesIO(response.content)
                                video_bytes.name = new_posts.title + '.mp4'
                                print(video_bytes.name)
                                upvotes = new_posts.score
                                comments = new_posts.num_comments
                                print(upvotes)
                                bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_VIDEO)
                                bot.send_video(chat_id=xchatid, video=video_bytes, caption='['+subreddit_name+']  '+video_bytes.name+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                                time.sleep(2)
                            #   bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_VIDEO)
                                break
                    except Exception as e: 
                        print(e)
                        break
                # continue
                    

                if not new_posts.is_self and new_posts.url.endswith('.jpg'):
                    try:
                        response = requests.get(new_posts.url)
                        img = Image.open(BytesIO(response.content))
                        img.thumbnail((1024, 1024))
                        output = BytesIO()
                        upvotes = new_posts.score
                        comments = new_posts.num_comments
                        print(upvotes)
                        pictitle = new_posts.title + '.jpg'
                        img.save(output, format='JPEG')
                        photo_data = output.getvalue()
                        bot.send_chat_action(chat_id=xchatid, action=telegram.ChatAction.UPLOAD_PHOTO)
                        bot.send_photo(chat_id=xchatid, photo=photo_data, caption='['+subreddit_name+']  '+pictitle+'     '+f"👍 {upvotes} 💬 {comments}", reply_markup=inline_keyboard)
                        time.sleep(2)
                    #  bot.send_chat_action(chat_id=5362284509, action=telegram.ChatAction.UPLOAD_PHOTO)
                        break
                    except Exception as e: 
                        print(e)
                        break

                if "redgif" in new_posts.url:
                    print ("skipping")
                    
                    continue

except Exception as e: 
    print(e)
    '''

#bot.send_invoice(chat_id="5362284509", title= "Redditbot", currency="SEK", invoice_payload="cc", description="redditbot", provider_token="350862534:LIVE:YTBjNGU4OWIyNGQ0", prices = [LabeledPrice(label='Working Time Machine', amount=1100), LabeledPrice('Extra Fees', 0)])
def handle_pre_checkout_query(update, context):
    query = update.pre_checkout_query
    if query.invoice_payload == 'cc':
        # The invoice is valid, so answer with True to indicate that the payment can be processed
        print("success")
        context.bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    else:
        # The invoice is invalid, so answer with False and an error message
        context.bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=False, error_message='Invalid invoice')
        print("failed")
def handle_successful_payment(update, context):
    today = date.today()
    date_string = today.strftime("%Y-%m-%d")
    falsedate = "FALSE   " + date_string
    truedate = "TRUE   " + date_string
    global paiduser
    message = update.message
    # Extract payment information from the message
    payment_info = message.successful_payment
    # Access the payment provider's API to check if the payment was successful
    # If the payment was successful, deliver the product/service to the user
    # Otherwise, handle the payment failure as appropriate
    # In this example, we'll just send a message indicating the payment status
    if payment_info.total_amount == 100:
        bot.send_message(chat_id=xchatid, text="Payment successful! Premium user privileges granted.")
        message.reply_text("Payment successful! Thank you for your purchase.")
        paiduser = True
        try:
            conn = mariadb.connect(
                user="richa",
                password="opop",
                host="192.168.8.114",
                port=3306,
                database="telebot"
            )
            print("Connection successful!")
            time.sleep(2)
            print("Writing to MariaDB")
            cur = conn.cursor()
            # Define the SQL query to insert data into the 'users' table
            query = "INSERT INTO users (member, id, premium) VALUES (?, ?, ?)"

            # Define the values to be inserted into the query
            values = (membername, xchatid, truedate)

            # Execute the query with the values
            cur.execute(query, values)

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

            
                   

        
    else:
        try:
                conn = mariadb.connect(
                    user="richa",
                    password="opop",
                    host="192.168.8.114",
                    port=3306,
                    database="telebot"
                )
                print("Connection successful!")
                time.sleep(2)
                print("Writing to MariaDB")
                cur = conn.cursor()
                # Define the SQL query to insert data into the 'users' table
                query = "INSERT INTO users (member, id, premium) VALUES (?, ?, ?)"

                # Define the values to be inserted into the query
                values = (membername, xchatid, falsedate)

                # Execute the query with the values
                cur.execute(query, values)

                # Commit the changes to the database
                conn.commit()

                # Close the cursor and connection
                cur.close()
                conn.close()
                
               
        except Error as e:
                    print(f"Error connecting to MariaDB Platform: {e}")
        bot.send_message(chat_id=xchatid, text="Payment unsuccessful. Please contact support.")
        message.reply_text("Payment failed. Please contact support.")        
# Add the pre-checkout query handler to the dispatcher
dispatcher.add_handler(PreCheckoutQueryHandler(handle_pre_checkout_query))
dispatcher.add_handler(MessageHandler(Filters.successful_payment, handle_successful_payment))


'''

       
        #continue
        

   


#bot.infinity_polling()
'''
