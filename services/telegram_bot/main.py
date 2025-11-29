import logging
import asyncio
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from db import Database
from bot_logic import generate_response

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Initialize DB
db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I can recommend what to wear based on the weather. Just tell me your location.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    
    # Save user message
    db.add_message(user_id, "user", user_text)
    
    # Get history
    history = db.get_history(user_id)
    # Remove the last message (current one) from history to avoid duplication if get_history includes it
    # My get_history implementation fetches the last N messages. 
    # Since I just added the message, it will be in the history.
    # bot_logic.generate_response adds the user message to the prompt manually.
    # So I should pass history EXCLUDING the current message, OR modify bot_logic.
    
    # Let's adjust bot_logic to NOT add the user message if it's already in history.
    # Or simpler: Pass history excluding the last message.
    
    history_context = history[:-1] if history else []
    
    # Generate response
    try:
        response_text = generate_response(user_text, history_context)
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        response_text = "Sorry, I encountered an error."

    # Save model response
    db.add_message(user_id, "model", response_text)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

if __name__ == '__main__':
    TELEGRAM_TOKEN = config("TELEGRAM_BOT_TOKEN", default="YOUR_TOKEN_HERE")
    
    if TELEGRAM_TOKEN == "YOUR_TOKEN_HERE":
        print("Error: TELEGRAM_BOT_TOKEN not found in .env")
        exit(1)
        
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    print("Bot is running...")
    application.run_polling()
