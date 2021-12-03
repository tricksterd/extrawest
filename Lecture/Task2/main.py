from decimal import Decimal


def saveToFile(fileName, value):
    with open('Results/' + fileName, 'w') as file:
        file.write(str(value))


def findMaxInt():
    maxInt = 2
    while True:
        try:
            maxInt = maxInt ** maxInt
        except MemoryError:
            saveToFile('MaxInt.txt', maxInt)
            return None


def findMinInt():
    minInt = -2
    while True:
        try:
            minInt = (minInt ** abs(minInt)) * -1
        except MemoryError:
            saveToFile('MinInt.txt', minInt)
            return None


def floatWithMoney():
    return 0.1 + 0.1 + 0.1


def decimalWithMoney():
    number = Decimal("0.1")
    return number + number + number


def maxString():
    testStr = ' '
    while True:
        try:
            testStr = testStr * (1 + len(testStr))
        except MemoryError:
            saveToFile('MaxLenStr.txt', str(len(testStr)))
            return None


def sizeOfBool():
    pass
