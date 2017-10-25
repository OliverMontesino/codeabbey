import sys

count = sys.stdin.readline()

for x in range(0, int(count)):

    sides = sys.stdin.readline()
    sides = sides.split(" ")

    side1 = int(sides[0])
    side2 = int(sides[1])
    side3 = int(sides[2])

    if (side1 + side2) > side3 and (side3 + side2) > side1 and (side3 + side1) > side2:
        print(1, " ")
    else:
        print(0, " ")
