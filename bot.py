import telebot
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6517290687:AAFtTp7poDBMVrJXXJJvetJ63dDeLQG7Ais')

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    welcome_message = "Welcome to my bot by: @fxe_68"
    bot.send_message(message.chat.id, welcome_message)

# Handle Instagram Reel links
@bot.message_handler(regexp=r'https?://(?:www\.)?instagram\.com/.*?/reel/.*')
def handle_reel_link(message):
    try:
        # Extract the link from the message
        link = message.text

        # Download the video from the link
        response = requests.get(link)
        
        # Replace 'video.mp4' with an appropriate filename
        with open('video.mp4', 'wb') as video_file:
            video_file.write(response.content)

        # Send the downloaded video back to the user
        video = open('video.mp4', 'rb')
        bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

# Start the bot
bot.polling()
