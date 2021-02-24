#packeage_48619016 21 Feb 2021, 11:40:24
import operator


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, num):
        return self.stack.append(num)

    def pop(self):
        try:  
            return self.stack.pop()
        except IndexError:
            raise IndexError('Stack is empty!') 


OPERATORS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv
} 


class Calculator:
    def __init__(self, array, operators=OPERATORS):
        self.array = array
        self.operators = operators

    def calculation(self, stack=None):
        stack = Stack() if stack is None else stack
        for item in self.array:
            if item in self.operators:
                second_num = stack.pop() 
                first_num = stack.pop() 
                stack.push(self.operators[item](first_num, second_num))
            else:
                try:
                    stack.push(int(item))
                except ValueError as error:
                    raise ValueError(f'{error} - Item is not num!')
        return stack.pop()


if __name__ == '__main__': 
    array = input().split()            
    stack = Stack() 
    print(Calculator(array, OPERATORS).calculation(stack))
