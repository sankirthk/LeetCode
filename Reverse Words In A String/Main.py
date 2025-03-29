class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()

        reversedList = wordList[::-1]

        reversedString = " ".join(reversedList)

        return reversedString

if __name__ == "__main__":
    s = "the sky is blue"
    solution = Solution()
    print(f"Output is: {solution.reverseWords(s)}")