import telebot
from instaloader import Instaloader, Profile, Post

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6517290687:AAFtTp7poDBMVrJXXJJvetJ63dDeLQG7Ais')

# Initialize Instaloader
loader = Instaloader()

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    welcome_message = "Welcome to my bot by: @fxe_68\nPlease send your Instagram video link."
    bot.send_message(message.chat.id, welcome_message)

# Handle Instagram video links
@bot.message_handler(regexp=r'https?://(?:www\.)?instagram\.com/p/.*|https?://(?:www\.)?instagram\.com/tv/.*')
def handle_instagram_video_link(message):
    try:
        # Extract the link from the message
        link = message.text

        # Determine the post type (photo, video)
        post = Post.from_shortcode(loader.context, link.split("/")[-1])
        
        if post.is_video:
            # Download the video
            loader.download_post(post, target=post.owner_username)
            video_filename = f"{post.owner_username}/{post.shortcode}.mp4"

            # Send the downloaded video back to the user
            with open(video_filename, 'rb') as video_file:
                bot.send_video(message.chat.id, video_file)
        else:
            bot.reply_to(message, "This link is not for an Instagram video.")

    except Exception as e:
        bot.reply_to(message, "We couldn’t handle your request. Please check the provided link or try again later.")

# Start the bot
bot.polling()
