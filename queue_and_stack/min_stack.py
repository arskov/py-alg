"""
This is the example of the implementaton of the MinStack.
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Test sequence is [2,3,1,2,1,0]

>>> st = MinStack()
>>> st.push(2)
>>> st.top()
2
>>> st.push(3)
>>> st.top()
3
>>> st.getMin()
2
>>> st.push(1)
>>> st.top()
1
>>> st.getMin()
1
>>> st.push(2)
>>> st.top()
2
>>> st.getMin()
1
>>> st.push(1)
>>> st.top()
1
>>> st.getMin()
1
>>> st.push(0)
>>> st.top()
0
>>> st.getMin()
0
>>> st.pop()
>>> st.pop()
>>> st.pop()
>>> st.top()
1
>>> st.getMin()
1
"""
class MinStack:

    def __init__(self):
        self._list = []
        self._min_list = []

    def push(self, x: int) -> None:
        self._list.append(x)
        if not self._min_list or x <= self._min_list[-1]:
            self._min_list.append(x)
    
    def pop(self) -> None:
        x = self._list.pop()
        if x == self._min_list[-1]:
            self._min_list.pop()

    def top(self) -> int:
        return self._list[-1]

    def getMin(self) -> int:
        return self._min_list[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)