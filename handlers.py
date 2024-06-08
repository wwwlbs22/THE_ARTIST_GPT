# handlers.py
from telegram import Update
from telegram.ext import CallbackContext
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your AI-powered bot. How can I assist you today?')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Here are the commands you can use:\n/start - Start the bot\n/help - Get help')

def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming messages and respond with AI-generated text."""
    user_message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=150
    )
    reply = response.choices[0].text.strip()
    update.message.reply_text(reply)

