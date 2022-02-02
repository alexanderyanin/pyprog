print()
print('Для расчета индекса массы тела (ИМТ)', end='\n\n')
weight = int(input('- укажите ваш вес (кг): '))
print()
height = int(input('- укажите ваш рост (см): '))
height_m = height/100  # переводим рост из сантиметров в метры
bmi = weight // (height_m * height_m)
print()
print('Ваш ИМТ: ≈', bmi, 'кг/м²', end='\n\n')
if bmi <= 16:
    print('У вас выраженный дефицит массы тела', end='\n\n')
elif bmi >= 16 and bmi <= 18.5:
    print('У вас недостаточная (дефицит) масса тела', end='\n\n')
elif bmi >= 18.5 and bmi <= 25:
    print('У вас нормальная масса тела', end='\n\n')
elif bmi >= 25 and bmi <= 30:
    print('У вас избыточная масса тела', end='\n\n')
elif bmi >= 30 and bmi <= 35:
    print('У вас ожирение 1 степени', end='\n\n')
elif bmi >= 35 and bmi <= 40:
    print('У вас ожирение 2 степени', end='\n\n')
elif bmi >= 40:
    print('У вас ожирение 3 степени', end='\n\n')
