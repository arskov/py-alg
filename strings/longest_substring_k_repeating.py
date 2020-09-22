from collections import Counter
from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring T of a given string 
        (consists of lowercase letters only) such that every character in T
        appears no less than k times. 
        """
        if s is None or len(s) == 0:
            return 0
        counter = Counter(s)
        dic = defaultdict(int)
        
        def isValid():
            for v in dic.values():
                if v < k:
                    return False
            return True
        
        i = 0
        j = 0
        max_len = float("-inf")
        while j < len(s):
            if counter[s[j]] < k:
                # scan i - j for valid substring and update max_len so far if substring 
                # probably update counter minus values from dic
                # update i
            dic[s[j]] += 1
            j += 1
        return max_len + 1 if max_len != float("-inf") else 0        

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("bbaaacbd", 3))
    print(solution.longestSubstring("bbaaabcd", 3))
