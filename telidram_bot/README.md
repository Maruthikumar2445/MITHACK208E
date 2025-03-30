# Multilingual Telegram AI Assistant

A Telegram bot powered by Google's Gemini AI that supports multiple languages and handles both text and image queries.

## Features

- **Multilingual Support** 🌐
  - English 🇬🇧
  - Hindi (हिंदी) 🇮🇳
  - Tamil (தமிழ்) 🇮🇳
  - Telugu (తెలుగు) 🇮🇳

- **Multi-Modal Capabilities**
  - Text conversations
  - Image analysis with captions
  - Language-specific responses

- **User Preferences**
  - Language selection persistence
  - Easy language switching with `/language` command

## Setup

### Prerequisites

```bash
python -m pip install --upgrade pip
pip install python-telegram-bot==13.7
pip install python-dotenv
pip install google-generativeai
pip install Pillow
pip install requests
```

### Environment Variables

Create a `.env` file in the project root:

```plaintext
TELEGRAM_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

### Configuration

The bot uses the following default configuration:

```python
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
```

## Usage

1. Start the bot:
```bash
python updated_bot.py
```

2. In Telegram:
   - Start a chat with the bot
   - Use `/start` or `/language` to select your preferred language
   - Send text messages or images with optional captions
   - Get AI-powered responses in your chosen language

## Commands

- `/start` - Initialize the bot and select language
- `/language` - Change your language preference

## Error Handling

The bot includes comprehensive error handling with:
- Language-specific error messages
- Fallback responses
- Logging for debugging

## Development

The main components are:
- `updated_bot.py` - Main bot logic
- Language dictionaries for responses
- Image processing capabilities
- Gemini AI integration

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for the language model
- Telegram Bot API
- Python Telegram Bot library