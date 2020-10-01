import math

class Solution:
    '''
    279. Perfect Squares
    
    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

    n = 12
    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
    0   1   2   3   1   2   3   4   2   1   2   3   3   2   3
    '''
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [i for i in range(n + 1)]
        for x in range(4, n + 1):
            if self.is_square(x):
                dp[x] = 1
                continue
            for y in range(1, math.ceil(math.sqrt(x))):
                tmp = y * y
                if tmp > x:
                    break
                dp[x] = min(dp[x], 1 + dp[x - tmp])
        return dp[n]
    
    def is_square(self, n: int) -> bool:
        sq = math.sqrt(n)
        fl = math.floor(sq)
        return ((sq - fl) == 0)

if __name__ == "__main__":
    solution = Solution()

    for i in range(17):
        print(i, "is a square", solution.is_square(i))

    for i in range(15):
        print(i, " => ", solution.numSquares(i))
