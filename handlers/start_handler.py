import re
from characterai import aiocai, sendCode, authUser

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from filters.chat_type import ChatTypeFilter
from config.config import OWN_ID, OWN_ID_2
from states.states import Login
from databases import database

start_router: Router = Router()
domen_link = 'https://character.ai/'
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

@start_router.message(StateFilter(None), ChatTypeFilter(chat_type=["private"]), Command('cancel'))
async def cmd_cancel_no_state(message: Message, state: FSMContext) -> None:
    await state.set_data({})
    await message.answer("Operation not cancelled!")


@start_router.message(ChatTypeFilter(chat_type=["private"]), Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext = "*") -> None:
    await state.clear()
    await message.answer("Operation cancelled!")


@start_router.message(StateFilter(None), ChatTypeFilter(chat_type=["private"]), CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    if message.from_user.id == OWN_ID or message.from_user.id == OWN_ID_2:
        await message.reply("Hello! Before we start a conversation, you need to log in. Please begin by sending me your email address.")
        await state.set_state(Login.email)


@start_router.message(
        F.text.func(lambda email: not re.fullmatch(regex, email)),
        Login.email, 
        ChatTypeFilter(chat_type="private")
)
async def email_incorrectly(message: Message) -> None:
    await message.reply("Invalid email. Try again: ")


@start_router.message(Login.email, ChatTypeFilter(chat_type="private"))
async def email_sended(message: Message, state: FSMContext) -> None:
    user_email = message.text
    _ = sendCode(user_email)
    await state.update_data(email=user_email)
    await message.reply("Great! I’ve sent a link to your email. Please send that link back to me.")
    await state.set_state(Login.link)


@start_router.message(
        F.text.func(lambda message: not message.startswith(domen_link)),
        Login.link, 
        ChatTypeFilter(chat_type="private")
)
@start_router.message(
        F.text.func(lambda message: not message.startswith(domen_link)),
        Login.chat, 
        ChatTypeFilter(chat_type="private")
)
async def link_or_chat_incorrectly(message: Message) -> None:
    await message.reply("Invalid pur link He must be in the form of https://character.ai/... Try again: ")


@start_router.message(Login.link, ChatTypeFilter(chat_type="private"))
async def link_sended(message: Message, state: FSMContext) -> None:
    user_link = message.text
    await state.update_data(link=user_link)
    await message.reply("Well done! The last step is to send me the link to the chat with the character you want to talk to. (The link should start like this: <code>https://character.ai/chat/...</code>)")
    await state.set_state(Login.chat)


@start_router.message(Login.chat, ChatTypeFilter(chat_type="private"))
async def chat_sended(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    user_data = await state.get_data()
    
    char_id = message.text.split(domen_link + 'chat/')[1]
    try: 
        ch_token = authUser(user_data['link'], user_data['email'])
        if ch_token:
            client = aiocai.Client(ch_token)
            me = await client.get_me()
            async with await client.connect() as chat:
                new_chat, answer = await chat.new_chat(
                    char_id, me.id, greeting="Hello, my darling ✨"
                )
                await database.add_data(user_id, ch_token, char_id, new_chat.chat_id)
                await message.reply("That’s it! You can now start chatting with the character. <b>Enjoy your conversation!</b>")
                await message.answer(answer.text)
        else: 
            await message.reply("You are not authorized!")
        await state.clear()
    except Exception as e:
        print(e)
        await message.reply("Invalid link or email. Try again: ")
        await state.set_state(Login.email)
        await state.set_data({})
        await message.answer("Hello! Before we start a conversation, you need to log in. Please begin by sending me your email address.")
