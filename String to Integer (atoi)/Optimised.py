
class Solution:
    def myAtoi(self, s: str) -> int:
            
        INT_MIN  = -2**31
        INT_MAX = 2**31 - 1
       
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i+=1
        
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '+' or s[i] == '-':
            
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        result = 0

        while i < n and self.isnum(s[i]):
            result = result * 10 + int(s[i])
            i += 1
        
        result = result * sign

        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result

    def isnum(self, c):
        return ord('0') <= ord(c) <= ord('9')
    
if __name__ == "__main__":
    input1 = " -421bvcs"
    solution = Solution()
    print(f"Input is: {input1}")
    print(f"Output is: {solution.myAtoi(input1)}")
        
        