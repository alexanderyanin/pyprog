# TODO  добавить инструкции по шагам
#       добавить сообщение при вводе 0

counter = 5  # 5 будни - 2 выходные
num = int(input('\nВведи оценку, полученную на прошлой неделе:\n\n'))
while num != 0:
    num = int(input())
    if num == 2:
        counter = counter - 2
    elif num == 3:
        counter = counter - 1
    elif num == 4:
        counter = counter + 1
    elif num == 5:
        counter = counter + 2
    elif num == 1:
        print('Кажется на этой неделе кто-то остался без игр\n')
    elif num < 0 or num > 5:
        print('Таких оценок еще не придумали\n')
print('\nНа эту неделю у тебя', counter, 'часов для игр', end='\n\n')
