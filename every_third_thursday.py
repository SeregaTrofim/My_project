#Программа определяет все даты бесплатных дней посещения Эрмитажа
#В данном случае третий четверг месяца в введенном году и выводит их.
#Даты расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.

import calendar
from datetime import *

year = int(input())
c = 0
for i in range(1, 13):
    x = calendar.monthcalendar(year, i)
    c = 0
    for j in x:
        for s in j:
            if s == 0:
                continue
            else:
                d = date(year, i, s)
                if d.weekday() == 3:

                    c += 1
                    if c == 3:
                        print(d.strftime('%d.%m.%Y'))