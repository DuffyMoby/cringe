from bruh import Stack
from operator import add, sub, mul, truediv, pow
test = '2 2 3 + * '
operators = {'+': add, '-': sub, '*': mul, '/': truediv, '**': pow}
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3, '(' : 4, ')' : 5}
def evaluate(arg):
    stack = Stack()
    list = arg.split()
    for i in list:
        if i not in operators:
            stack.push(i)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.push(operators[i](a,b))
            
    return stack.main

def translate(arg):
    list = arg.split()
    stack = Stack()
    output = ''
    for i in list:
        if i not in precedence:
            output += i + ' ' 
        else:
            if i == '(':
                stack.push(i)
            elif i == ')':
                while stack.top() != '(':
                    output += stack.pop() + ' ' 
                stack.pop()
            elif not stack.main or stack.top() == '(':
                stack.push(i)
            elif precedence[i] > precedence[stack.top()] or i == '**':
                stack.push(i)
            elif precedence[i] <= precedence[stack.top()] :
                while stack.main and precedence[i] <= precedence[stack.top()]:
                    output += stack.pop() + ' ' 
                stack.push(i)
    for i in stack.main:
        output += stack.pop() + ' '
    
    return output

print(translate('2 * 2 + 10 - ( 3 * 4 )'))


            
        



print(evaluate(test))
