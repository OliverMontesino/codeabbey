import sys

count = sys.stdin.readline()

for x in range(0, int(count)):
    numbers = sys.stdin.readline()
    numbers = numbers.split(" ")
    division = int(numbers[0]) / int(numbers[1])
    rounded = round(division)
    print(rounded)
    print(" ")
