import telebot
from telebot import types
import constants.constants as const
from weather_utils.weather_service import WeatherService


bot = telebot.TeleBot(const.TELEGRAM_BOT_TOKEN)
service = WeatherService()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    print('User wants to start')
    keyboard_markup = types.InlineKeyboardMarkup()
    button_today = types.InlineKeyboardButton('heute', callback_data='today')
    button_tomorrow = types.InlineKeyboardButton('morgen', callback_data='tomorrow')
    keyboard_markup.add(button_today, button_tomorrow)

    print(m)
    bot.send_message(m.chat.id, 'Wetter für...', reply_markup=keyboard_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  # в call.data хранится то сообщение, которое мы указали в кнопках на втором месте
  # id вашего чата хранится в call.from_user.id
  print(call)
  if call.data == "today":
    bot.send_message(call.from_user.id, service.get_weather_for_city('Bobingen'))
  elif call.data == "tomorrow":
    bot.send_message(call.from_user.id, "for tomorrow")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print('User wrote text')
    bot.send_message(message.chat.id, 'Hello, world!')


if __name__ == '__main__':
    if not const.is_token_set():
        raise RuntimeError('Tokens are not set')

    bot.remove_webhook()
    bot.polling(none_stop=True, interval=0)
