import sys

count = sys.stdin.readline()
count = int(count)
sum = 0

for x in range(0, count):
    numbers = sys.stdin.readline()
    numbers = numbers.split(" ")
    sum = int(numbers[0]) + int(numbers[1])
    print(sum)
    print(" ")
