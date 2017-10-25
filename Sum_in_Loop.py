import sys

count = sys.stdin.readline()
numbers = sys.stdin.readline()
numbers = numbers.split(" ")
sum = 0
for number in numbers:
    sum = sum + int(number)
print(sum)
