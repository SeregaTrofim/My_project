#Реализована функция num_of_sundays(), которая принимает на вход один аргумент
#year — натуральное число, год
#Функция возвращает количество воскресений в году year

from datetime import *

def num_of_sundays(year):
    # year = int(input())

    m_date = date(year, 1, 1)
    x = timedelta(days=365)
    n_date = m_date + x

    if m_date.weekday() == 6 or (n_date.year == year and m_date.weekday() == 5):
        return 53
    else:
        return 52