class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        charMap = ["" for _ in range(numRows)]

        index = 0 
        step = 1

        for char in s:

            charMap[index] += char

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            
            index += step
        
        return "".join(charMap)
    
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    print(f"Output is {solution.convert(s, numRows=numRows)}")