class Solution:
    def longestPalindrome(self, s: str) -> str:

        output = ""

        for i in range(len(s)):

            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)

            if len(odd) > len(output):
                output = odd
            elif len(even) > len(output):
                output = even
        
        return output
    
    def expand(self, s:str, left: int, right: int) -> str:
        while left>=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

if __name__ == "__main__":
    input1 = "babad"
    solution = Solution()
    print(f"Output is: {solution.longestPalindrome(input1)}")