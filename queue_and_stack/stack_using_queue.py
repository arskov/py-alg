"""
225. Implement Stack using Queues
Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:

    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

>>> s = MyStack()
>>> s.push(1)
>>> s.top()
1
>>> s.push(2)
>>> s.top()
2
>>> s.push(3)
>>> s.top()
3
>>> s.push(4)
>>> s.top()
4
>>> s.push(5)
>>> s.top()
5
>>> s.pop()
5
>>> s.pop()
4
>>> s.push(6)
>>> s.pop()
6
>>> s.pop()
3
>>> s.pop()
2
>>> s.pop()
1
"""
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.straight_queue = deque()
        self.reversed_queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.reversed_queue:
            self.straight_queue.append(self.reversed_queue.popleft())
        self.reversed_queue.append(x)
        while self.straight_queue:
            self.reversed_queue.append(self.straight_queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.reversed_queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.reversed_queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.reversed_queue else False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)