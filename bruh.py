
class Stack():
    def __init__(self):
        self.main = []
    
    def push(self, item):
        self.main.append(item)

    def pop(self):
        self.temp = self.main.pop()
        return self.temp

    def top(self):
        return self.main[-1]

class Queue():
    def __init__(self):
        self.main = []

    def enqueue(self,item):
        self.main.append(item)

    def dequeue(self):
        return self.main.pop(0)

class LinkedList():
    def __init__(self):
        self.main = []
    
    def append(self, item):
        self.main.append(item)
    
    def insert(self, item, index):
        self.main.insert(index,item)
    
    def pop(self):
        return self.main.pop()

    def remove(self,index):
        self.main.remove(index)

        

    

