import numbers

class Calculator:
    """
    This is a basic calculator for simple operations including addition, subtraction, multiplication, division and nth root
    
    """
    def __init__(self):
        self.memory = 0

    def check_input(self, input):
        if not isinstance(input, numbers.Number):
            raise TypeError(f'"{input}" was not a number. Input a real number')

    def reset(self):
        self.memory = 0
        return self.memory
    
    def add(self, num: int)-> int:
        self.check_input(num)
        self.memory += num
        return self.memory
    
    def subtract(self,num: int)-> int:
        self.check_input(num)
        self.memory -= num
        return self.memory

    def multiply(self, num: int)-> int:
        self.check_input(num)
        self.memory *= num
        return self.memory

    def divide(self, num: int)-> float:
        self.check_input(num)
        self.memory *= num
        return self.memory

    def divide(self, num):
        self.check_input(num)
        try:
            self.memory /= num
            return self.memory
        except ZeroDivisionError:
            raise ZeroDivisionError('cannot divide by zero')

    def nth_root(self, root: int, num= None) -> float:
        if num == None:
            self.memory **= (1/root)
            return round(self.memory, 1)
        else:
            result = num ** (1/root)
            return round(result, 2)

