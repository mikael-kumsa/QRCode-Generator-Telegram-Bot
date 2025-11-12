import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
from qr_generator import generateQR
import random
# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define conversation state
ASK_CONTENT = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler."""
    await update.message.reply_text(
        "👋 Hi there! What do you want the content of you QR Code to be?"
    )
    return ASK_CONTENT


async def main_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Receive user's content and send back the qrcode."""
    content = update.message.text
    user = update.message.from_user
    user_name = user['username']
    file_suffix = random.randint(1, 900)
    path = user_name + str(file_suffix) + ".png"
    qr = generateQR(content, path)
    # Send a personalized message
    await update.message.reply_text(f"Generating...")
    # Send an image (URL or local file)
    image_url = qr
    await update.message.reply_photo(photo=image_url, caption="Here's your QR code")
    # End conversation
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Conversation cancelled.")
    return ConversationHandler.END


def main():
    """Run the bot."""
    app = Application.builder().token(BOT_TOKEN).build()
    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_action)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)
    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
