from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


btnSearch = KeyboardButton('🔎')
btnLyrics = KeyboardButton("Search by Lyrics")
btnBack = KeyboardButton("🔙")
backMenu = ReplyKeyboardMarkup().add(btnBack)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSearch,btnLyrics)