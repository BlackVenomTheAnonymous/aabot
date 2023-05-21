import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater


# Function to handle the "/start" command
def start(update: Update, context: CallbackContext):
    # Send a welcome message with the command list
    welcome_message = "Welcome to the bot! Here are the available commands:\n\n/grab - Use this command to grab details."
    update.message.reply_text(welcome_message)


# Function to handle the "/grab" command
def grab(update: Update, context: CallbackContext):
    # Extract the necessary details from the command
    command_args = update.message.text.split()[1:]
    if len(command_args) >= 5:
        cs, pk, amount, email, stripe_link = command_args[:5]
        
        # Compose the message with the extracted details
        message_text = f"CS: {cs}\nPK: {pk}\nAmount: {amount}\nEmail: {email}"
        
        # Create the inner line button
        inner_line_button = InlineKeyboardButton(text="𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」", url="https://t.me/xerrox_army")
        reply_markup = InlineKeyboardMarkup([[inner_line_button]])
        
        # Send the composed message to the user
        update.message.reply_text(text=message_text, reply_markup=reply_markup)
    else:
        update.message.reply_text("Invalid command. Please provide all required details.")


# Function to handle any other message
def echo(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I don't understand that command. Use /help to see the available commands.")


def main():
    # Initialize the Telegram Bot
    updater = Updater("6270334389:AAG_D9igT5TJesW24SVOZtjGe7BNGlNh7Bg", use_context=True)
    dispatcher = updater.dispatcher

    # Set up handlers for commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("grab", grab))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
