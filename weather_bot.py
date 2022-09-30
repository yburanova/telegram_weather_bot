import telebot
from telebot import types
import constants.constants as const
from weather_utils.weather_service import WeatherService


bot = telebot.TeleBot(const.TELEGRAM_BOT_TOKEN)
service = WeatherService()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    print('User wants to start')
    user_first_name = m.from_user.first_name
    message = f'Hallo, {user_first_name}! Was möchtest du tun?'

    keyboard_markup = types.InlineKeyboardMarkup()
    button_today = types.InlineKeyboardButton('Wetterbericht für heute', callback_data='today')
    keyboard_markup.add(button_today)

    print(m)
    bot.send_message(m.chat.id, message, reply_markup=keyboard_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  # в call.data хранится то сообщение, которое мы указали в кнопках на втором месте
  # id вашего чата хранится в call.from_user.id
  print(call)
  if call.data == "today":
    bot.send_message(call.from_user.id, 'Bitte, die Stadt oder den Ortsnamen schreiben')
  elif call.data == "tomorrow":
    bot.send_message(call.from_user.id, "for tomorrow")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(f'User wrote text: {message}')
    suppose_to_be_cityname = message.text
    bot.send_message(message.chat.id, service.get_weather_for_city(suppose_to_be_cityname), parse_mode='html')


if __name__ == '__main__':
    if not const.is_token_set():
        raise RuntimeError('Tokens are not set')

    bot.remove_webhook()
    bot.polling(none_stop=True, interval=0)
