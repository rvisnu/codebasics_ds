"""
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""

from collections import deque

class AssessBrackets:
    def __init__(self):
        self.brackets = deque()
        self.curly = deque()
        self.box = deque()
        
    def _is_empty(self):
        if len(self.brackets) or len(self.curly) or len(self.box):
            return False
        return True
        
    def is_balanced(self, equation_to_check):
        push_item = {
            "(": self.brackets,
            "{": self.curly,
            "[": self.box
        }
        pop_item = {
            ")": self.brackets,
            "}": self.curly,
            "]": self.box
        }
        
        for item in equation_to_check:
            if item in push_item.keys():
                push_item[item].append(item)
            elif item in pop_item.keys():
                if not pop_item[item]:
                    return False
                pop_item[item].pop()
        return self._is_empty()
        
test = AssessBrackets()
    
print(test.is_balanced("({a+b})"))
print(test.is_balanced("))((a+b}{"))
print(test.is_balanced("((a+b))"))
print(test.is_balanced("))"))
print(test.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
        
        
    
