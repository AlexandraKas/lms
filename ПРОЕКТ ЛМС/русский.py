from random import randint as rd
import enchant


spisok = []
stroka = ''

try:
    file = open('ПРЕПРИ.txt', 'r')
    stroka = file.read()
    spisok = stroka.split()
except FileNotFoundError:
    file = open('ПРЕПРИ.txt', 'w')
else:
    file.close()


if spisok != []:
    while True:
        
        dl = len(spisok)
        pos = rd(0, dl-1)
    
        word = spisok[pos]

        c = enchant.Dict("ru_RU")
        print("Введите правильно слово: ", word)
       
        a= input('')
        print(c.check(a))
