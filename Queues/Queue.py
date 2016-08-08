'''
 simple queue implementation
'''
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None 


    def __str__(self):
        return str(self.queue)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) is 0:
            return True
        return False



#testing 
queue = Queue()
print(str(queue.dequeue()))
queue.enqueue(4)
queue.enqueue(7)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(9)
queue.enqueue(0)
queue.enqueue(41)
queue.enqueue(74)

print(str(queue.dequeue()))
queue.dequeue()
queue.enqueue(9)

print (str(queue))
