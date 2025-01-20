from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        singlestr = ""
        for string in strs:
            singlestr += string + '#'
        return singlestr
    def decode(self, s: str) -> List[str]:
        result = []
        string = ""
        for letter in s:
            if letter != '#':
                string += letter
            else:
                result.append(string)
                string = ""
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
