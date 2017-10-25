import sys

count = sys.stdin.readline()
count = int(count)

for x in range(0, count):
    numbers = sys.stdin.readline()
    numbers = numbers.split(" ")
    firstValue = int(numbers[0])
    stepSize = int(numbers[1])
    numOfFirstValuesAccounted = int(numbers[2])
    chainNumber = [firstValue]
    dinamicNumber = firstValue + stepSize

    for num in range(1, numOfFirstValuesAccounted):
        chainNumber.append(dinamicNumber)
        dinamicNumber = dinamicNumber + stepSize

    total = sum(chainNumber)
    print(total, " ")
