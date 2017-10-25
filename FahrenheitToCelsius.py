import sys

numbers = sys.stdin.readline()
numbers = numbers.split(" ")
count = int(numbers[0])

for f in range(0, count+1):
    c = (int(numbers[f]) - 32) * (5 / 9)
    c = round(c)
    print(c)
    print(" ")
