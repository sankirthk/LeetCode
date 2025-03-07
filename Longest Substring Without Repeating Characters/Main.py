from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charCount = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in charCount:
                l = max(charCount[s[r]] + 1, l)
            charCount[s[r]] = r
            res = max(res, r - l + 1)
        return res
            
if __name__ == "__main__":
    s = "dvdfe"
    solution = Solution()
    print("Input: ", s)
    print("Output: ", solution.lengthOfLongestSubstring(s))