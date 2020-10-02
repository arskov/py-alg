"""
232. Implement Queue using Stacks

>>> q = MyQueue()
>>> q.push(1)
>>> q.peek()
1
>>> q.push(2)
>>> q.peek()
1
>>> q.push(3)
>>> q.peek()
1
>>> q.push(4)
>>> q.peek()
1
>>> q.push(5)
>>> q.peek()
1
>>> q.pop()
1
>>> q.pop()
2
>>> q.push(6)
>>> q.pop()
3
>>> q.pop()
4
>>> q.pop()
5
>>> q.pop()
6
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.reversed_stack = []
        self.straight_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.reversed_stack:
            self.straight_stack.append(self.reversed_stack.pop())
        self.straight_stack.append(x)
        while self.straight_stack:
            self.reversed_stack.append(self.straight_stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.reversed_stack.pop()        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.reversed_stack[-1]       
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.reversed_stack else False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)