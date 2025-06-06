class Solution:
    def reverse(self, x: int) -> int:

        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        
        return sign * rev

        # sign = [1, -1][x < 0]
        # x = abs(x)
        # output = []
        # while x:
        #     x, mod = divmod(x, 10)
        #     output.append(str(mod))
        
        # output = int("".join(output))
        # return output*sign

    
if __name__ == "__main__":
    x = -123
    solution = Solution()
    print(f"Output is: {solution.reverse(x)}")