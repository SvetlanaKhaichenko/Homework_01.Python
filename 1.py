# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

week = int(input('Введите цифру дня недели: \n'))

if week == 7 or week == 6:
    print('Ура, выходной!')
elif week > 7:
    if week%7==0:
        print('Ура, выходной!')
    elif week%6==0:
        print('Ура, выходной!')
    else:
        print ('Рабочий день')
else:
        print ('Рабочий день')
