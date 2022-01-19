import wolframalpha
import telebot, emoji, time, jdatetime
from pytz import timezone


#********************************************************************************
#********************************************************************************

# importing token
TOKEN = ""

# initializing bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'Start'])
def start(message):

  name = message.from_user.first_name
  TEXT =  " خوش اومدی رفیق متقلب من " +emoji.emojize(" :winking_face_with_tongue: ")
  bot.send_message(chat_id=message.chat.id, text=TEXT )

@bot.message_handler(commands=['help', 'Help'])
def help(message):

    TEXT = emoji.emojize(" :blue_circle: ")
    TEXT += "به این نمونه ها نگاه کن تا دستت بیاد  \n\n"
    TEXT += "برای اینکه جواب رو بصورت عکس داشته باشی میتونی آخر دستور "
    TEXT +="\n+img"
    TEXT += "اضافه کنی (آخرین نمونه رو ببین)"
    bot.send_message(chat_id=message.chat.id, text=TEXT )
    url_manual_image = "https://i.postimg.cc/pLvrnn8v/manual-wolfram-bot.jpg"
    bot.send_photo(chat_id=message.chat.id, photo=url_manual_image)

# *************************************************************************
##***************************************************************************
#****************************************************************************

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
	bot.reply_to(message, " جدا فکر کردی میتونی با استیکر فرستادن منو دست بنداری؟ ")

@bot.message_handler(content_types=['photo', 'audio', 'video', 'voice', "document", 'video_note', 'location'])
def PAV_handler(message):
	bot.reply_to(message, " خب الان من با این چی کنم ")

@bot.message_handler(content_types=['animation'])
def gif_handler(message):
    bot.reply_to(message, text="(@magatowski) گیف هاتو بفرست برای مهدی ")

# *************************************************************************
##***************************************************************************
#****************************************************************************
@bot.message_handler(content_types=['text'])
def main_handler(message):
	main(message)

# add the sleep and restarting

def main(message):
    allowed_users = ['Magatowski', 'busybusy22', 'ayrozz', 'mahdi_shahini', 'Morteza_24']

    chat_ID = message.chat.id

    jdatetime.set_locale('fa_IR')
    info_line =  " " + jdatetime.datetime.now(timezone("Asia/Tehran")).strftime("%c")
    print("\n" + message.from_user.username, info_line)


    if message.from_user.username != None and  message.from_user.username in allowed_users :

        message = message.text.lower()

        image_or_not = 0
        if "+img" in message:
            message = message[:-4]
            image_or_not = 1

        question = message
        # App id obtained by the above steps
        app_id = ''

        # Instance of wolf ram alpha
        # client class
        client = wolframalpha.Client(app_id)

        # Stores the response from
        # wolf ram alpha
        res = client.query(question)

        if image_or_not == 1:
            for pod in res.pods:
                for sub in pod.subpods:
                    img_url = sub.img.src
                    bot.send_photo(chat_id=chat_ID, photo=img_url)

        else :
            ans = next(res.results).text

            if '=' in ans :
                print(ans)
                i = ans.find("=")
                fst, snd = ans[0:i], ans[i+1:]
                TEXT = emoji.emojize(" :red_circle: ") + fst + ' = \n\n' + emoji.emojize(" :green_circle: ") +snd
                bot.send_message(chat_id=chat_ID, text=TEXT)

            else :
                TEXT = emoji.emojize(" :red_circle: ") + ans
                bot.send_message(chat_id=chat_ID, text=TEXT)

    else:
        TEXT = 'دسترسی داده نمی شود. برای استفاده از ربات باید آیدی شما در لیست باشد'
        TEXT += '\n\n به مهدی بگو اضافه کنه آيدیتو'
        TEXT +='\n  ** @magatowski ** '
        bot.send_message(chat_id=chat_ID, text=TEXT)

# ****************************************************************
#*****************************************************************

# ****************************************************************
#*****************************************************************

try:
    bot.infinity_polling()
except Exception:
    time.sleep(15)


# *************************************************************************
##***************************************************************************
#****************************************************************************

