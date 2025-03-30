import os
import logging
import telebot
from telebot import types
import google.generativeai as genai
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API Keys
TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini with generation config
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-002',  # Updated to latest available model
    generation_config=generation_config
)

# Add user language preference storage
user_languages = {}

SUPPORTED_LANGUAGES = {
    'english': 'English 🇬🇧',
    'hindi': 'हिंदी 🇮🇳',
    'tamil': 'தமிழ் 🇮🇳',
    'telugu': 'తెలుగు 🇮🇳'
}

WELCOME_MESSAGES = {
    'english': "Welcome! I'm your AI Assistant. How can I help you today? 🤖",
    'hindi': "नमस्ते! मैं आपका AI सहायक हूं। आज मैं आपकी कैसे मदद कर सकता हूं? 🤖",
    'tamil': "வணக்கம்! நான் உங்கள் AI உதவியாளர். இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்? 🤖",
    'telugu': "నమస్కారం! నేను మీ AI సహాయకుడిని. నేడు నేను మీకు ఎలా సహాయం చేయగలను? 🤖"
}

def get_gemini_response(prompt, image_url=None, language='english'):
    try:
        # Add language context with improved language handling
        context = {
            'english': "You are an AI assistant. Respond in English. Be helpful and informative.",
            'hindi': "आप एक AI सहायक हैं। हिंदी में जवाब दें। सहायक और जानकारीपूर्ण बनें।",
            'tamil': "நீங்கள் ஒரு AI உதவியாளர். தமிழில் பதிலளிக்கவும். உதவிகரமாகவும் தகவல் நிறைந்ததாகவும் இருங்கள்.",
            'telugu': "మీరు AI సహాయకులు. తెలుగులో సమాధానం ఇవ్వండి. సహాయకరంగా మరియు సమాచారపూరితంగా ఉండండి."
        }

        # Set context based on user's language
        selected_context = context.get(language, context['english'])
        formatted_prompt = f"{selected_context}\n\nUser Query: {prompt}"
        
        if image_url:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            model_response = model.generate_content([formatted_prompt, img])
        else:
            model_response = model.generate_content(formatted_prompt)
        
        if hasattr(model_response, 'text'):
            logger.info(f"Generated response in {language}")
            return model_response.text
        if hasattr(model_response, 'parts'):
            return model_response.parts[0].text
            
        # Fallback messages in different languages
        fallback_messages = {
            'english': "Sorry, I couldn't generate a response.",
            'hindi': "क्षमा करें, मैं जवाब नहीं दे पा रहा हूं।",
            'tamil': "மன்னிக்கவும், எனக்கு பதில் உருவாக்க முடியவில்லை.",
            'telugu': "క్షమించండి, నేను సమాధానం ఇవ్వలేకపోయాను."
        }
        return fallback_messages.get(language, fallback_messages['english'])
        
    except Exception as e:
        logger.error(f"Error calling Gemini API: {e}")
        error_messages = {
            'english': "An error occurred while processing your request.",
            'hindi': "आपके अनुरोध को संसाधित करते समय एक त्रुटि हुई।",
            'tamil': "உங்கள் கோரிக்கையை செயலாக்கும்போது பிழை ஏற்பட்டது.",
            'telugu': "మీ అభ్యర్థనను ప్రాసెస్ చేస్తున్నప్పుడు లోపం సంభవించింది."
        }
        return error_messages.get(language, error_messages['english'])

# Initialize bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'language'])
def select_language(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    language_buttons = [types.KeyboardButton(lang_name) for lang_name in SUPPORTED_LANGUAGES.values()]
    markup.add(*language_buttons)
    bot.reply_to(
        message,
        "Please select your preferred language / कृपया अपनी पसंदीदा भाषा चुनें / மொழியை தேர்ந்தெடுக்கவும் / భాష ఎంచుకోండి:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text in SUPPORTED_LANGUAGES.values())
def set_language(message):
    user_id = message.from_user.id
    selected_lang = next(k for k, v in SUPPORTED_LANGUAGES.items() if v == message.text)
    user_languages[user_id] = selected_lang
    
    # Send welcome message in selected language
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.reply_to(message, WELCOME_MESSAGES[selected_lang], reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        user_id = message.from_user.id
        language = user_languages.get(user_id, 'english')
        
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        
        prompt = message.caption if message.caption else "Analyze this image"
        
        logger.info(f"Received image with prompt: {prompt}")
        response = get_gemini_response(prompt, file_url, language)
        bot.reply_to(message, response)
        
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        bot.reply_to(message, "Sorry, I couldn't process that image.")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    if message.text in SUPPORTED_LANGUAGES.values():
        return
        
    user_id = message.from_user.id
    if user_id not in user_languages:
        select_language(message)
        return
        
    logger.info(f"Received message: {message.text}")
    response = get_gemini_response(message.text, language=user_languages[user_id])
    bot.reply_to(message, response)

if __name__ == "__main__":
    logger.info("Bot started")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(f"Bot error: {e}")