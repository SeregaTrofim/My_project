#Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
#Программу принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

#На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

#Программа выводит текст с указанием количества дней и часов, оставшихся до выхода курса.

from datetime import *
def choose_plural(amount, declensions):
    a = [2, 3, 4]
    if amount % 10 == 1 and (amount % 100) // 10 != 1:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in a and (amount % 100) // 10 != 1:
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'
#(("день", "дня", "дней"), ("час", "часа", "часов"), ("минута", "минуты", "минут"))
course_start = datetime(2022, 11, 8, 12)

current_dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
diff = course_start - current_dt

days = diff.days
hours = diff.seconds // 3600
minutes = (diff.seconds // 60) % 60

if current_dt > course_start or current_dt == course_start:
    print('Курс уже вышел!')
else:
    if days > 0:
        if hours > 0:
            if minutes > 0:
                print(f'До выхода курса осталось: {choose_plural(days,("день", "дня", "дней"))} и {choose_plural(hours,("час", "часа", "часов"))}')
            else:
                print(f'До выхода курса осталось: {choose_plural(days,(("день", "дня", "дней")))}')
        else:
            print(f'До выхода курса осталось: {choose_plural(days,(("день", "дня", "дней")))}')
    else:
        if hours > 0:
            if minutes > 0:
                print(f'До выхода курса осталось: {choose_plural(hours,(("час", "часа", "часов")))} и {choose_plural(minutes, (("минута", "минуты", "минут")))}')
            else:
                print(f'До выхода курса осталось: {choose_plural(hours,(("час", "часа", "часов")))}')
        else:
            if minutes > 0:
                print(f'До выхода курса осталось: {choose_plural(minutes, (("минута", "минуты", "минут")))}')