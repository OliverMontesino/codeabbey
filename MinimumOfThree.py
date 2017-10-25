import sys

count = sys.stdin.readline()

for x in range(0, int(count)):
    numbers = sys.stdin.readline()
    numbers = numbers.split(" ")
    if int(numbers[0]) < int(numbers[1]):
        if int(numbers[0]) < int(numbers[2]):
            print(" %s" % numbers[0])
        else:
            print(" %s" % numbers[2])
    else:
        if int(numbers[1]) < int(numbers[2]):
            print(" %s" % numbers[1])
        else:
            print(" %s" % numbers[2])
