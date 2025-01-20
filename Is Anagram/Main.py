from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordS = {}
        wordT = {}
        if len(s) != len(t):
            return False
        
        for charS, charT in zip(s, t):
            wordS[charS] = 1 + wordS.get(charS, 0)
            wordT[charT] = 1 + wordT.get(charT, 0)
        
        for char in wordS:
            if char not in wordT:
                return False
            if wordS[char] != wordT[char]:
                return False
        return True



# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = "racecar"
    input2 = "carrace"
    print("Input List:", input1, input2)
    output = solution.isAnagram(input1, input2)
    print("Output List:", output)