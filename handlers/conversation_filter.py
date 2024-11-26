from characterai import aiocai

from aiogram import Router, F, flags
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from config.config import OWN_ID, OWN_ID_2
from databases import database

conversation_router: Router = Router()


@conversation_router.message(F.text, ChatTypeFilter(chat_type=["private"]))
@flags.chat_action("typing")
async def conversation_router_filter(message: Message):
    user_id = message.from_user.id
    if message.from_user.id == OWN_ID or message.from_user.id == OWN_ID_2:
        user_text = message.text

        ch_token = await database.get_data(user_id, 'ch_token')
        char_id = await database.get_data(user_id, 'char_id')
        chat_id = await database.get_data(user_id, 'chat_id')

        if ch_token:
            client = aiocai.Client(ch_token)

            async with await client.connect() as chat:
                ch_message = await chat.send_message(
                    char_id, chat_id, user_text
                )
            
            await message.answer(ch_message.text)
        else: 
            await message.reply("You are not authorized! Please, enter the command /start.")