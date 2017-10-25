import sys

count = sys.stdin.readline()

for i in range(0, int(count)):
    numbers = sys.stdin.readline()
    numbers = numbers.split()
    total = 0
    sumDigits = 0

    total = int(numbers[0]) * int(numbers[1]) + int(numbers[2])

    for digit in str(total):
        sumDigits += int(digit)

    print(sumDigits, " ")
