print('Напишите любое натуральное число без пробелов, программа заменит все цифры на слова')
n = input()
d = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}
for i in range(len(n)):
    if n[i] in d:
        print(d[n[i]], end=' ')
x = input()