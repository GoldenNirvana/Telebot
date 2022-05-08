import telebot

f = 0

bot = telebot.TeleBot('5219483490:AAG1_zB0MxWTgZZNc0gM3ptlOqd1soLBjns')

symbols = ['\U000025AA', '\U0001f3a5']


@bot.message_handler()
def get_text(message):
    global f
    if message.text == "Волосы":
        f = 1
        return
    if message.text == "Зарплата":
        f = 2
        return

    count_of_worid = 0
    text = message.text
    arrayText = text.split()
    prev = "1"
    for word in arrayText:
        a = word[0] in symbols
        b = count_of_worid == 1
        c = (prev[0] in symbols)
        d = word[len(word) - 1] == ':'
        if a or b or c and d:
            if word[0] == '\U0001f3a5':
                count_of_worid = 1
            if word[0] == '\U000025AA':
                count_of_worid = 2
            stri = "<b>" + word + "</b>"
            text = text.replace(word, stri, 1)
        prev = word

    tex = '\U0001F4E9' + "Отправить заявку на кастинг:"
    text = text.replace(tex, "<b>" + tex + "</b>")

    hairs = "\n\n<b>ПРИМЕЧАНИЕ ОТ ЧАТА NEW CASTING:</b> Девушки берегите свои волосы, подобная работа может испортить вам волосы"
    plat = "\n\n<b>ПРИМЕЧАНИЕ ОТ ЧАТА NEW CASTING:</b> БУДЬТЕ ОСТОРОЖНЫ, ВЫСОКИЙ ГОНОРАР МОЖЕТ БЫТЬ УЛОВКОЙ МОШЕННИКОВ"

    if f == 1:
        text = text + hairs
    if f == 2:
        text = text + plat

    f = 0
    bot.send_message(message.chat.id, text, parse_mode='html')
    raise ValueError("yra")


def main():
    while True:
        try:
            bot.polling(none_stop=True)
        finally:
            print("w")
            main()


if __name__ == '__main__':
    main()
