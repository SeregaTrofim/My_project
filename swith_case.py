#Программа получает на вход строку - название знака зодиака и затем сообщает к какому типу относится введенный знак.
#Логика определения следующая:

#если введут любое из значений Овен, Лев, Стрелец, то программа выводит текст Огненный
#если введут любое из значений Телец, Дева, Козерог, то программа выводит текст Земной
#если введут любое из значений Близнецы, Весы, Водолей, то программа выводит текст Воздушный
#если введут любое из значений Рак, Скорпион, Рыбы, то программа выводит текст Водный

match input():
    case 'Овен' | 'Лев' | 'Стрелец':
        print('Огненный')
    case 'Телец' | 'Дева' | 'Козерог':
        print('Земной')
    case 'Близнецы' | 'Весы' | 'Водолей':
        print("Воздушный")
    case 'Рак' | 'Скорпион' | 'Рыбы':
        print('Водный')