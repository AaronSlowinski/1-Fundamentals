class Queue:
    def __init__(self):
        self.item = []
        
    def size (self):
        return len(self.item)
    
    def enqueue (self,item):
        self.item.append(item)
    
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.item.pop(0)
    
    def show_queue(self):
        print(self.item)
        
q= Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print ("Pass" if (q.size() == 3) else ("Fail"))
q.enqueue('d')

print ("Pass" if (q.size() == 4) else ("Fail"))

print ("Pass" if (q.dequeue() == 'a') else ("Fail"))
print ("Pass" if (q.dequeue() == 'd') else ("Fail"))
print ("Pass" if (q.size() == 2) else ("Fail"))      

q.show_queue()