from typing import List 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
    
        # Initialize result list and character maps
        result = []
        pCount = {}
        sCount = {}
        
        # Count characters in pattern p
        for char in p:
            pCount[char] = 1 + pCount.get(char, 0)
        
        # Initialize sliding window
        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        # Check if first window is an anagram
        if pCount == sCount:
            result.append(0)
        
        # Slide the window
        for i in range(len(p), len(s)):
            # Add new character from right
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
            # Remove leftmost character
            left_char = s[i - len(p)]
            sCount[left_char] -= 1
            
            # Clean up zero counts
            if sCount[left_char] == 0:
                del sCount[left_char]
            
            # Check if current window is an anagram
            if pCount == sCount:
                result.append(i - len(p) + 1)
        
        return result
            
