from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            w = "".join(sorted(word))
            mp.setdefault(w,[]).append(word)
        
        return list(mp.values())
    
if __name__=="__main__":
    input1 = ["eat","tea","tan","ate","nat","bat"]
    solution = Solution()
    print(f"Input: {input1}")
    print(f"Output: {solution.groupAnagrams(input1)}")
        