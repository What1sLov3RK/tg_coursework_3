import aiogram
from aiogram import executor
import requests
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.types import file
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons as nav
import os
from pytube import YouTube

PATH = os.getcwd()
MUSIC_ROOT = os.path.join(PATH, 'music')

if not os.path.exists(MUSIC_ROOT):
    os.makedirs(MUSIC_ROOT)

# Initialize the bot and dispatcher
bot = aiogram.Bot()
dp = Dispatcher(bot, storage=MemoryStorage())

class States(StatesGroup):
    BASE = State()
    MUSIC = State()
    LYRICS = State()


@dp.message_handler(state ='*', commands=['start'])
async def search_song_by_title(message):
    await bot.send_message(message.chat.id,"Hello, I'm cool bot for searching and saving music, use buttons below to"+
                                           "interact with me!",reply_markup=nav.mainMenu)
    await States.BASE.set()

@dp.message_handler(state = States.BASE)
async def echo_send(message: types.Message):
    if message.text == 'Search by Lyrics':
        await bot.send_message(message.from_user.id, "Input some lyrics", reply_markup=nav.backMenu)
        await States.LYRICS.set()
    if message.text == '🔎':
        await bot.send_message(message.from_user.id, "Input song title or author", reply_markup=nav.backMenu)
        await States.MUSIC.set()

# Search for a song by title
@dp.message_handler(state = States.MUSIC)
async def search_song_by_title(message: types.Message):
    title = message.text
    if title == '🔙' :
        await States.BASE.set()
        await bot.send_message(message.from_user.id,"Ok, what else?",reply_markup=nav.mainMenu)
    else:
        url, name = find_song_by_title(title)
        pathes = YouTube(url).streams.filter(only_audio=True).first().download(output_path=MUSIC_ROOT)
        with open(pathes, "rb") as mp3:
            await bot.send_audio(message.from_user.id, title=name, audio=mp3)

@dp.message_handler(state = States.LYRICS)
async def search_song_by_lyrics(message: types.Message):
    lyrics = message.text
    if lyrics == '🔙' :
        await States.BASE.set()
        await bot.send_message(message.from_user.id,"Ok, what else?",reply_markup=nav.mainMenu)
    else:
        video_url, full_name = find_song_by_lyrics(lyrics)
        pathes = YouTube(video_url).streams.filter(only_audio=True).first().download(output_path=MUSIC_ROOT)
        with open(pathes, "rb") as mp3:
            await bot.send_audio(message.from_user.id, title=full_name, audio=mp3)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)

def find_song_by_title(title):
    # Use the YouTube API to search for the song by title
    if title:
        params = {
            "part": "snippet",
            "q": title,
            "type": "video",
            "key":
        }

        response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
        data = response.json()
        video_url = f"https://www.youtube.com/watch?v={(data['items'][0]['id']['videoId'])}"
        full_name = data["items"][0]["snippet"]["title"]
        return video_url, full_name
    else:
        raise ValueError("no input")
        return "https://www.youtube.com/watch?v=0mV2rxqMCik", "FACE - Статус"

def find_song_by_lyrics(lyrics):
    if lyrics:
        params = {
            "part": "snippet",
            "q": lyrics,
            "type": "video",
            "key": 
        }

        response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
        data = response.json()
        video_url = f"https://www.youtube.com/watch?v={(data['items'][0]['id']['videoId'])}"
        full_name = data["items"][0]["snippet"]["title"]
        return video_url, full_name
    else:
        raise  ValueError("No input")
        return "https://www.youtube.com/watch?v=0mV2rxqMCik", "FACE - Статус"


