import logging
from telegram import Update
from telegram.ext import Application, CommandHandler
from telegram.error import NetworkError

logging.basicConfig(level=logging.INFO)

# Replace this with your actual Telegram Bot Token
TOKEN = "8129404848:AAGD-P2u7fxYs10wVpTmzTPAKn-KANENvec"

# Start command
async def start(update: Update, context) -> None:
    await update.message.reply_text(
        "🌱 Welcome to Helping Query Bot!\n"
        "I'm here to provide AI-driven agricultural insights.\n\n"
        "Use /help to see available commands."
    )

# Help command
async def help_command(update: Update, context) -> None:
    commands = """
🤖 **Available Commands:**
/start - Begin interaction with the bot
/help - Get a list of available commands
/fertilizer - Get recommendations on fertilizer usage
/pestcontrol - Receive pest alerts and pesticide suggestions
/irrigation - Get optimal irrigation schedules
/crophealth - Analyze crop health using NDVI
/farmertype - Check if you are a smallholder or large-scale farmer
/accessibility - Check access to farming resources
/affordability - Assess affordability concerns
/about - Learn more about this AI-driven agriculture bot
    """
    await update.message.reply_text(commands)

# Fertilizer recommendation
async def fertilizer(update: Update, context) -> None:
    await update.message.reply_text(
        "🧪 Based on soil conditions, I recommend:\n"
        "- **Nitrogen**: 50kg/ha\n"
        "- **Phosphorus**: 30kg/ha\n"
        "- **Potassium**: 20kg/ha"
    )

# Pest control alerts
async def pestcontrol(update: Update, context) -> None:
    await update.message.reply_text(
        "🐛 Pest alert! High risk of infestation detected. "
        "Recommended pesticide: **Neem-based bio-pesticide**."
    )

# Irrigation schedule
async def irrigation(update: Update, context) -> None:
    await update.message.reply_text(
        "💧 Optimal irrigation schedule:\n"
        "- Morning: **6:00 AM - 9:00 AM**\n"
        "- Evening: **4:00 PM - 7:00 PM**"
    )

# Crop health check using NDVI
async def crophealth(update: Update, context) -> None:
    await update.message.reply_text(
        "🌾 NDVI-based analysis:\n"
        "- Healthy Crops: ✅ 0.7 - 1.0\n"
        "- Moderate Health: ⚠️ 0.4 - 0.7\n"
        "- Poor Health: ❌ Below 0.4"
    )

# Farmer type classification
async def farmertype(update: Update, context) -> None:
    await update.message.reply_text(
        "👨‍🌾 Based on economic conditions:\n"
        "- **High-income farmers** → Large-Scale\n"
        "- **Low-income farmers** → Smallholder"
    )

# Accessibility check
async def accessibility(update: Update, context) -> None:
    await update.message.reply_text(
        "🌍 Accessibility Check:\n"
        "If you face difficulty accessing farming resources, reply **Yes**, otherwise reply **No**."
    )

# Affordability concern
async def affordability(update: Update, context) -> None:
    await update.message.reply_text(
        "💰 Affordability Check:\n"
        "If cost is a concern for farming inputs, reply **Yes**, otherwise reply **No**."
    )

# About the bot
async def about(update: Update, context) -> None:
    await update.message.reply_text(
        "🚜 Helping Query Bot provides AI-driven insights on **irrigation, pest control, fertilizers, and crop health** for farmers in India."
    )

# Main function to run the bot
def main():
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("fertilizer", fertilizer))
        application.add_handler(CommandHandler("pestcontrol", pestcontrol))
        application.add_handler(CommandHandler("irrigation", irrigation))
        application.add_handler(CommandHandler("crophealth", crophealth))
        application.add_handler(CommandHandler("farmertype", farmertype))
        application.add_handler(CommandHandler("accessibility", accessibility))
        application.add_handler(CommandHandler("affordability", affordability))
        application.add_handler(CommandHandler("about", about))
        application.run_polling()
    except NetworkError as e:
        logging.error(f"Network error occurred: {e}")

# Run the bot
if __name__ == "__main__":
    main()
