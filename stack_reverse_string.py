from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, string_value):
        reverse_string = ""
        for item in string_value:
            self.push(item)
        while not self.is_empty():
            reverse_string += self.pop()
        return reverse_string
        
        
my_stack = Stack()
print(my_stack.reverse_string("We will conquere COVID-19"))
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
