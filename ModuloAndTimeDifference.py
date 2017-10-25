import sys

count = sys.stdin.readline()

for i in range(0, int(count)):
    numbers = sys.stdin.readline()
    numbers = numbers.split(" ")
    totalSeconds1 = 0
    totalSeconds2 = 0
    days = 0
    hours = 0
    minutes = 0

    # Conversion a segundos del tiempo 1
    totalSeconds1 = totalSeconds1 + int(numbers[0]) * 86400  # dias a segundos
    totalSeconds1 = totalSeconds1 + int(numbers[1]) * 3600  # horas a segundos
    totalSeconds1 = totalSeconds1 + int(numbers[2]) * 60  # minutos a segundos
    totalSeconds1 = totalSeconds1 + int(numbers[3])  # sumamos segundos

    # Conversion a segundos del tiempo 2
    totalSeconds2 = totalSeconds2 + int(numbers[4]) * 86400  # dias a segundos
    totalSeconds2 = totalSeconds2 + int(numbers[5]) * 3600  # horas a segundos
    totalSeconds2 = totalSeconds2 + int(numbers[6]) * 60  # minutos a segundos
    totalSeconds2 = totalSeconds2 + int(numbers[7])  # sumamos segundos

    # Calculamos diferencia

    difference = totalSeconds2 - totalSeconds1
    if difference >= 86400:
        days = difference // 86400
        difference -= days*86400
    if difference >= 3600:
        hours = difference // 3600
        difference -= hours*3600
    if difference >= 60:
        minutes = difference // 60
        difference -= minutes*60

    print("({0} {1} {2} {3})".format(days, hours, minutes, difference))
    print(" ")
