from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            length = len(string)
            encodedStr += str(length) + '#' + string
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodedString.append(s[i:j])
            i = j
        return decodedString

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:", input1)
    encodedstring = solution.encode(input1)
    print("EncodedString:", encodedstring)
    print("Output:", solution.decode(encodedstring))

    # Test Case 3: Single string
    input3 = ["hello"]
    print("\nInput:", input3)
    encodedstring = solution.encode(input3)
    print("EncodedString:", encodedstring)
    print("Output:", solution.decode(encodedstring))

    # Test Case 4: Strings with no anagrams
    input4 = ["abc", "def", "ghi"]
    print("\nInput:", input4)
    encodedstring = solution.encode(input4)
    print("EncodedString:", encodedstring)
    print("Output:", solution.decode(encodedstring))