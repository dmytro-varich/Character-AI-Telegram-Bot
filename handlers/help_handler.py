from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeFilter
from config.config import OWN_ID, OWN_ID_2
from texts.texts import info_message

from databases.database import add_data
help_router: Router = Router()


@help_router.message(ChatTypeFilter(chat_type=["private"]), Command('info'))
async def cmd_help(message: Message) -> None:
    if message.from_user.id == OWN_ID or message.from_user.id == OWN_ID_2:
        await message.reply(info_message)