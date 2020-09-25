import argparse
import os
def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--word', type=str)
    p.add_argument('--file', type=str)
    return p

def making_algorifm(file):  #преобразуем прочитанный файл
  algrifm = file.read().replace('\n', ';').replace(' ', '')
  return algrifm + ';'

def step_inf(str, old, new):          #бесконечная операция
  while str.find(old) != -1:
    str = str.replace(old, new)
  return str

def step_fin(str, old, new):         #конечная операция
  str = str.replace(old, new, 1)
  return str

def normal_algorifm(word_list,file):
    origin_algrifm = making_algorifm(file) #нормальный алгорифм
    while word_list != '':
        f = word_list.index(';')
        str1 = str3 = str2 = word_list[:f] # номер окончания слова
        word_list = word_list[(f + 1):] # удаление слова из списка слов
        i = 0
        while i!= 2:
          algrifm = origin_algrifm
          while algrifm != '':
            n = algrifm.index('-') #номер вхождения символа "-"
            old = algrifm[:n]  # подстрока, которую нужно заменить
            if (str1.find(old) != -1 and algrifm[n+2]=='.'): #нашлась подстрока и точка
                m = algrifm.index(';')  # номер окончания единичного алгорифма
                new = algrifm[(n + 3):m]  # подстрока, на которую заменяют
                str1 = step_fin(str1, old, new)  # применяем функцию, которая меняет в каждой строке по правилу
                algrifm = algrifm[(m + 1):]  # переходим на новую строку в алгорифме
                i=2
                break
            else:
              m = algrifm.index(';') #номер окончания единичного алгорифма
              old = algrifm[:n] #подстрока, которую нужно заменить
              new = algrifm[(n + 2):m] #подстрока, на которую заменяют
              str1 = step_inf(str1, old, new) #применяем функцию, которая меняет в каждой строке по правилу
              algrifm = algrifm[(m + 1):]  # переходим на новую строку в алгорифме
          if(old == 'E' and str2 == str1):  #замена пустого элемента
            str1 = new + str1
            str2 = str1
          str1 = str1.replace('E', '') #убираем все потенциально пустые элементы
        print('Your word',str3,'become',str1)

    print('End of the program')

parser = parser_args()
word_list = parser.parse_args().word + ';'  # слово или список слов, которое нужно изменить
file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file), encoding="utf - 8")  # открываем файл с нормальным алгорифмом
if(word_list == "test;" and making_algorifm(file) == "test;"):
    word_list1 = '11;'
    file1 = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'algorifm1.txt'), encoding="utf - 8")
    normal_algorifm(word_list1, file1)
    word_list2 = 'IIIIIIIII;'
    file2 = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'algorifm5.txt'), encoding="utf - 8")
    normal_algorifm(word_list2, file2)
    word_list3 = 'aaa;'
    file3 = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'algorifm2.txt'), encoding="utf - 8")
    normal_algorifm(word_list3, file3)
else:
    normal_algorifm(word_list, file)