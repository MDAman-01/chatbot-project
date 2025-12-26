import telebot
Token='8569895432:AAFUdrltA6TJd8dohAGeY7gy0DRPaWG_llc'

bot=telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"welcome to Amancode_bot")



@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "This is use to calculator then feel free to ask")
@bot.message_handler()
def custom(message):
    try:
        msg=eval(message.text.strip())
    except Exception as e:
        msg="this can't be evaluated"
    bot.reply_to(message,msg)




 
 
 
 
bot.polling()