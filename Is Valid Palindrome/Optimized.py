class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isalphanum(s[l]):
                l+=1
            while r > l and not self.isalphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isalphanum(self, c: chr) -> chr:
        return (ord('0') <= ord(c) <= ord('9')
                or ord('a') <= ord(c) <= ord('z')
                or ord('A') <= ord(c) <= ord('Z'))

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = "Was it a car or a cat I saw?"
    print("Input:", input1)
    output = solution.isPalindrome(input1)
    print("Output:", output)