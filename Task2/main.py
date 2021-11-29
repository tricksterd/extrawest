from decimal import Decimal


def save_to_file(fileName, value):
    with open('Results/' + fileName, 'w') as file:
        file.write(str(value))


def find_max_int():
    max_int = 2
    while True:
        try:
            max_int = max_int ** max_int
        except MemoryError:
            save_to_file('MaxInt.txt', max_int)
            return None


def find_min_int():
    min_int = -2
    while True:
        try:
            min_int = (min_int ** abs(min_int)) * -1
        except MemoryError:
            save_to_file('MinInt.txt', min_int)
            return None


def float_with_money():
    return 0.1 + 0.1 + 0.1


def decimal_with_money():
    number = Decimal("0.1")
    return number + number + number


def max_string():
    test_str = ' '
    while True:
        try:
            test_str = test_str * (1 + len(test_str))
        except MemoryError:
            save_to_file('MaxLenStr.txt', str(len(test_str)))
            return None


def size_of_bool():
    pass
