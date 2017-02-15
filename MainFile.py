import math


def check_type(value, try_type, error):
    if isinstance(value, try_type):
        return True
    raise TypeError(error)


class SolveForX:
    def __init__(self, y, z):

        if check_type(y, (int, float), "y should be a number"):
            self.y = y

        if check_type(z, (int, float), "z should be a number"):
            self.z = z

    def multiply(self):
        """
        :param: self
        :return: int
        Assumes x * y = z, knowing y and z, solves for x
        """
        # self.y != 0 unless self.z == 0
        if self.y == 0 and self.z != 0:
            return print("Sorry! You cannot divide by zero and zero divided by anything is zero, but your 'z' is not. "
                         "'x' is not solvable.")

        elif self.y == 0 and self.z == 0:
            print("Sorry! You cannot divide by zero and zero divided by anything is zero; since your 'z' is zero"
                  "'x' is also zero.")
            x = 0
            return x

        else:
            x = self.z / self.y
            return x

    def divide(self):
        """
        :param: self
        :return: int
        Assumes x / y = z, knowing y and z, solves for x
        """
        # self.y != 0 unless assume x and y switch and self.z == 0
        if self.y == 0 and self.z != 0:
            return print("Sorry! You cannot divide by zero and zero divided by anything is zero, but your 'z' is not. "
                         "'x' is not solvable even if you switch x and y.")

        elif self.y == 0 and self.z == 0:
            print("Sorry! You cannot divide by zero and zero divided by anything is zero; since your 'z' is zero"
                  "'x' is also zero assuming x and y are switched.")
            x = 0
            return x

        else:
            x = self.z * self.y
            return x

    def exponent(self):
        """
        :param: self
        :return: int
        Assumes y**x = z, knowing y and z, solves for x
        """
        # self.y >= 1
        if self.y == 0 and self.z != 0:
            return print("Sorry! Your 'y' is 0 and your 'z' is not. Nothing but zero can become 0 using exponents."
                         "'x' does not exist")

        elif self.z < 0:
            print("Sorry! No real number to any power will equal a negative number. The following x value "
                  "assumes the absolute value of your 'z'.")
            x = math.log(abs(self.z), abs(self.y))
            return x

        elif self.y == 0 and self.z == 0:
            return print("Sorry! Your 'y' is 0 and your 'z' is also 0."
                         "'x' could be anything.")

        else:
            x = math.log(self.z, abs(self.y))
            return x


class Sequence():
    def __init__(self, limit):
        if check_type(limit, (int, float), "your limit should be a number"):
            self.limit = limit
        self.empty_list = []
        self.fibonacci_sequence = []
        self.limit_value = None

    def fibonacci(self):
        """
        :param limit: int
        limit is the number of members of the fibonacci sequence one wishes to find
        :return: list
        list.len == limit-1
        """

        # Binet's formula
        # F_n = (y**n - x**n) / (y - x)
        # F_n = Our fibonacci number _ number in the sequence
        # y = (1 + 5**(1/2)) / 2
        # y = The Golden Ratio
        # x = - 1 / y
        # x = The Negative Inverse of the Golden Ratio
        # therefore F_n = (y**n - (-1 / y)**n) / 5**(1/2)

        n = 0
        golden_ratio = (1 + 5 ** (1 / 2)) / 2
        fibonacci_sequence = self.empty_list
        while n < self.limit:
            iteration = int((golden_ratio**n - (-1 / golden_ratio)**n) / 5**(1/2))
            fibonacci_sequence.append(iteration)
            n += 1
        self.fibonacci_sequence = fibonacci_sequence
        self.limit_value = fibonacci_sequence[-1]
        return self.limit_value
