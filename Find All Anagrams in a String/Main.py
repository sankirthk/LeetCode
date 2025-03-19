
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pCount = {}
        sCount = {}
        output = []

        for char in p:
            pCount[char] = 1 + pCount.get(char, 0)

        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        if sCount == pCount:
            output.append(0)
        
        for i in range(len(p), len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

            sCount[s[i - len(p)]] -= 1

            if sCount[s[i - len(p)]] == 0:
                del sCount[s[i - len(p)]]
            
            if sCount == pCount:
                output.append(i - len(p) + 1)
        
        return output

    
if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    print(f"Output is: {solution.findAnagrams(s, p)}")