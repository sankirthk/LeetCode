from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        # Check for edge case when there are less than 2 characters in the string
        if len(s) < 2:
            return False
        
        for char in s:
            # If the char is in the opening list then it is appended to a temp list
            if char in opening:
                temp.append(char)
            # If the char is part of the closing list then we check for corresponding paranthesis
            elif char in closing: 
                if len(temp) < 1:
                    return False
                var = temp.pop()
                if char == ')':
                    if var != '(':
                        return False
                elif char == ']':
                    if var != '[':
                        return False
                elif char == '}':
                    if var != '{':
                        return False
        if len(temp) == 0:
            return True
        else:
            return False



# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = "{{"
    print("Input List:", input1)
    print("Output:", solution.isValid(input1))
                    
