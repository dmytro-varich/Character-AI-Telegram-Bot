# 👾 Character AI Telegram Bot
This project demonstrates interaction with the API of the [Character AI](https://character.ai/) web application, as well as the structure and principles of Telegram bot development. It allows users to chat with a Character AI persona in [Telegram](https://web.telegram.org/) by sending and receiving messages via the API. The project is built using the [Unofficial Python API for Character.AI](https://github.com/kramcat/CharacterAI) and can serve as a foundation for developing custom bots that integrate AI characters into the messenger.

# 🗂️ Project Structure 
```
character-ai-telegram-bot/
│── config/ 
│   ├── config.py                # Environment variable storage
│── databases/ 
│   ├── database.py              # Database module
│── filters/ 
│   ├── chat_type.py             # Filter to determine the type of chat (group or private)
│── handlers/   
│   ├── conversation_filter.py   # Dialog filtering logic
│   ├── help_handler.py          # Handler for the /help command
│   ├── start_handler.py         # Handler for the /start command
│── states/ 
│   ├── states.py                # State detection for dialog management with the user
│── texts/ 
│   ├── texts.py                 # Stores text messages
│── requirements.txt             # List of project dependencies      
│── README.md                    # Project documentation
```

# 🎥 Demo Video
...

# 📌 More Info
The author of this project is Dmytro Varich. You can find more information about him and his projects on his Telegram channel [@varich_channel](https://t.me/varich_channel). For collaboration inquiries, feel free to contact him via LinkedIn ([dmytro-varich](https://www.linkedin.com/in/dmytro-varich/)) or email at varich.it@gmail.com.
This Telegram bot [@babyfooji_character_ai_bot](https://t.me/babyfooji_character_ai_bot) was created as a test bot and is accessible only to the project creator. This limitation exists because the current version allows the bot to interact with only one chat. However, the project can be adapted to enable a single bot to communicate with multiple users, where each user would have their own individual conversation with a specific character.
