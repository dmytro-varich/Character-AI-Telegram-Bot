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
        await add_data(OWN_ID_2, '5158003cfcb2b9dcf16d04eb2f95c53b262d57a3', 'MtZ9L2BaB7MVT4q6vV4_jrR9DWScuDUHM_0EE8BOAlM', '9a77ae26-e10f-4b20-a38c-1ee6a8cd7ebc')
        await message.reply(info_message)