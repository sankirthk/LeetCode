from tarfile import LENGTH_LINK
from typing import List
import re

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        singlestr = ""
        for string in strs:
            singlestr += str(len(string)) + '#' + string
        return singlestr
    
    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length]) 
            i = j + 1 + length
        return result
                
            
        
            
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = ["neet", "code", "love", "you"]
    
    print("Input List:", input1)
    encodedstring = solution.encode(input1)
    print("Encoded String:", encodedstring)
    decodedstring = solution.decode(encodedstring)
    print("Decoded String:", decodedstring)
