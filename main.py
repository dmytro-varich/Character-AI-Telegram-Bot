import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware

from config.config import TG_TOKEN
from handlers import start_handler, help_handler, conversation_filter
from databases.database import create_db

logger = logging.getLogger(__name__)
bot = Bot(TG_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage(), maintenance_mode=False)

async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Starting Bot...")

    await create_db()

    dp.include_routers(
        start_handler.start_router,
        help_handler.help_router,
        conversation_filter.conversation_router 
    )

    dp.message.middleware(ChatActionMiddleware())

    await dp.start_polling(bot, handle_signals=False)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
