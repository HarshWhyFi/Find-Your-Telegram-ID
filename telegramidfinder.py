import telebot
import time

# Initialize the bot with your token
bot_token = "YOUR-BOT-TOKEN-HERE"  # Replace this with your actual bot token
bot = telebot.TeleBot(bot_token)

# Define a command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else "N/A"  # Handle case when no last name is provided
    username = message.from_user.username if message.from_user.username else "N/A"  # Handle case when no username is provided

    # Send back a message with the user's ID, first name, last name, and username
    bot.reply_to(message, f"ðŸ‘‹ Hello, {first_name}! ðŸŽ‰ Here are your details:\n\n"
                          f"ðŸ”‘ User ID:  {user_id}\n"
                          f"ðŸ‘¤ First Name:  {first_name}\n"
                          f"ðŸ‘¥ Last Name:  {last_name}\n"
                          f"âœ… Username:  @{username}")

# Start the bot with exception handling
try:
    print("Bot is polling...")
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Error occurred: {e}")
    time.sleep(15)  # Wait 15 seconds before trying again
    bot.polling(none_stop=True)
