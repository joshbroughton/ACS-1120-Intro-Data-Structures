from linkedlist import LinkedList

class Queue(LinkedList):
    def enqueue(self, item):
        super().append(item)

    def dequeue(self):
        item = self.head
        self.head = self.head.next
        return item
    
    def iterate(self):
        return super().items()