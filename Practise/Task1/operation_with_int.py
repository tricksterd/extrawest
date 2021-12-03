class OperationWithInt:
    """this class created for practise with integers"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def degree(self):
        return self.a ** self.b

    def division(self):
        return self.a / self.b

    def int_division(self):
        return self.a // self.b

    def modulo_division(self):
        return self.a % self.b

    def left_shift(self):
        return self.a << self.b

    def right_shift(self):
        return self.a >> self.b

    def bit_and(self):
        return self.a & self.b

    def bit_or(self):
        return self.a | self.b

    def bit_exc_or(self):
        return self.a ^ self.b

    def bit_not(self):
        return ~self.a

    def less(self):
        return self.a < self.b

    def more(self):
        return self.a > self.b

    def less_or_equal(self):
        return self.a >= self.b

    def more_or_equal(self):
        return self.a <= self.b

    def equal(self):
        return self.a == self.b

    def not_equal(self):
        return self.a != self.b

