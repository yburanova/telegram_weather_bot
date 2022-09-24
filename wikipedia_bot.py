import telebot
import wikipedia
import re
import os

token = os.environ.get("TOKEN", "token not found!")
bot = telebot.TeleBot(token)
wikipedia.set_lang("ru")


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        print(ny)

        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        print(wikitext)

        # Разделяем по точкам . Текст может заканчиваться посреди предложения
        wikimas = wikitext.split('.')

        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]

        # Создаем пустую переменную для текста
        wikitext2 = ''

        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        # Возвращаем текстовую строку
        return wikitext2

    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    print('User wants to start')
    print(m)
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print('User wrote text')
    bot.send_message(message.chat.id,
                     'Hello, world!'
                     #getwiki(message.text)
                     )


# Запускаем бота
if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True, interval=0)
