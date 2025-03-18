
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        floor  = -2**31
        ceil = 2**31 - 1
        temp = ""
        strNotNum = 0

        noSpaceWord = s.lstrip()
        if noSpaceWord[0] == '-' or noSpaceWord[0] == '+':
            sign = -1
            strNum = noSpaceWord[1:]
        else:
            sign = 1
            strNum = noSpaceWord


        for char in strNum:
            if self.isnum(char):
                temp += char
            else:
                strNotNum
                break

        if temp != "":
            num = int(temp) * sign

            if num < floor:
                return floor
            if num > ceil:
                return ceil
            return num

        return 0
    
    def isnum(self, c):
        return ord('0') <= ord(c) <= ord('9')
    
if __name__ == "__main__":
    input1 = " "
    solution = Solution()
    print(f"Input is: {input1}")
    print(f"Output is: {solution.myAtoi(input1)}")
        
        