from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        postfix = [0] * n
        prefix[0] = postfix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        return result   


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [1,2,4,6]
    print("Input:", input1)
    output = solution.productExceptSelf(input1)
    print("Output:", output)

    '''# Test Case 3: Single string
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
    print("Output:", solution.decode(encodedstring))'''