"""
This is the example of the implementaton of the MaxStack.
Design a stack that supports push, pop, top, and retrieving the max element in constant time.
Test sequence is [1,2,3,1,2,2,3]

>>> st = MaxStack()
>>> st.push(1)
>>> st.top()
1
>>> st.push(2)
>>> st.top()
2
>>> st.getMax()
2
>>> st.push(3)
>>> st.top()
3
>>> st.getMax()
3
>>> st.push(1)
>>> st.top()
1
>>> st.getMax()
3
>>> st.push(2)
>>> st.top()
2
>>> st.getMax()
3
>>> st.push(2)
>>> st.top()
2
>>> st.getMax()
3
>>> st.push(3)
>>> st.top()
3
>>> st.getMax()
3
>>> st.pop()
>>> st.top()
2
>>> st.getMax()
3
>>> st.pop()
>>> st.top()
2
>>> st.getMax()
3
>>> st.pop()
>>> st.top()
1
>>> st.getMax()
3

"""
class MaxStack:

    def __init__(self):
        self._list = []
        self._max_list = []

    def push(self, x: int) -> None:
        self._list.append(x)
        if not self._max_list or x >= self._max_list[-1]:
            self._max_list.append(x)
    
    def pop(self) -> None:
        x = self._list.pop()
        if x == self._max_list[-1]:
            self._max_list.pop()

    def top(self) -> int:
        return self._list[-1]

    def getMax(self) -> int:
        return self._max_list[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)