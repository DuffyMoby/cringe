from bruh import Stack
test = '2 2 3 + * '
operators = ['+', '-', '*', '/']
def evaluate(arg):
    stack = Stack()
    list = arg.split()
    for i in list:
        if i not in operators:
            stack.push(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.push(b+a)
            elif i == '-':
                stack.push(b-a)
            elif i == '*':
                stack.push(b*a)
            elif i == '/':
                stack.push(b/a)

    return stack.main

print(evaluate(test))
