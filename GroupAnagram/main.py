from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for string in strs:
            alphabetcount = [0] * 26
            for character in string:
                alphabetcount[ord(character) - ord("a")] += 1
            
            anagram[tuple(alphabetcount)].append(string)
        
        return list(anagram.values())  # Convert to list since defaultdict.values() returns a dict view

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:", input1)
    print("Output:", solution.groupAnagrams(input1))

    # Test Case 2: Empty input
    input2 = []
    print("\nInput:", input2)
    print("Output:", solution.groupAnagrams(input2))

    # Test Case 3: Single string
    input3 = ["hello"]
    print("\nInput:", input3)
    print("Output:", solution.groupAnagrams(input3))

    # Test Case 4: Strings with no anagrams
    input4 = ["abc", "def", "ghi"]
    print("\nInput:", input4)
    print("Output:", solution.groupAnagrams(input4))