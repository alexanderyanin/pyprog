# TODO  добавить инструкции по шагам
#       добавить сообщение при вводе 0
counter = 7  # 7ч на неделю 5 будни и 2 выходные
#print('\nВведите оценку, полученную на прошлой неделе', end='\n\n')
num = int(input('\nВведи оценку, полученную на прошлой неделе:\n\n'))
while num != 0:
#for i in range(10):
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
