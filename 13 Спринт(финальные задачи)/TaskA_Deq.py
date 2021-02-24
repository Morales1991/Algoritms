#packeage_48613789 20 Feb 2021, 23:13:28

class Deque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0      
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value):
        if self.is_full():
            raise IndexError('error')
        self.tail = (self.tail + 1) % self.max_size
        self.deque[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise IndexError('error')
        self.head =(self.head - 1) % self.max_size
        self.deque[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('error')
        value = self.deque[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise IndexError('error')
        value = self.deque[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


def command_handler(parameters, commands):
    outputdata = []
    for command, *params in commands:
        try:
            temporary_variable = getattr(parameters, command)(*params)
        except IndexError as error:
            temporary_variable = 'error'
        except:
            raise AttributeError('error')
        if temporary_variable is not None:
            outputdata.append(temporary_variable)
    return outputdata  


if __name__ == '__main__':
    num = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    commands = [input().split() for _ in range(num)]
    result = command_handler(deque, commands)
    print(*result, sep='\n')
