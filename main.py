a = int(input('Введите результат первого дня: '))
b = int(input("Введите желаемый результат: "))

day = 1

while a < b:
    a = a * 1.1
    day = day + 1

print('Номер дня, в который будет достигнут желаемый результат: ', day)