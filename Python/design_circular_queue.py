"""
Use two pointers to keep track of front and rear of the queue
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.size = 0
        self.capacity = k
        
        self.front = 0
        self.rear = -1 
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
