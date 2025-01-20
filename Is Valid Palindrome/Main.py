class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        s = s.lower()
        for letter in s:
            if letter.isalnum():
                string += letter
        

        if string == string[::-1]:
            return True
        return False
    
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = "Was it a car or a cat I saw?"
    print("Input:", input1)
    output = solution.isPalindrome(input1)
    print("Output:", output)