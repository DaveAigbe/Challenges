class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[0] = value
            return True
        else:
            if self.isFull():
                return False
            else:
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = value
                return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if ((self.front + 1) % self.size) == self.rear:
                self.queue[self.front] = None
                self.front = -1
                self.rear = -1
                return True
            else:
                self.queue[self.front] = None
                self.front = (self.front + 1) % self.size
                return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return ((self.rear + 1) % self.size) == self.front


if __name__ == '__main__':
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1))  # return True
    print(myCircularQueue.enQueue(2))  # return True
    print(myCircularQueue.enQueue(3))  # return True
    print(myCircularQueue.enQueue(4))  # return False
    print(myCircularQueue.Rear())  # return 3
    print(myCircularQueue.isFull())  # return True
    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.enQueue(4))  # return True
    print(myCircularQueue.Rear())  # return 4
