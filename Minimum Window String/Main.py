class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        flag = False
        tVal = [char for char in t]
        if len(s) < len(t):
            return output
        
        for i in range(len(s)):
            if not flag:
                temp = [char for char in tVal]
                res = ""
                flag = True
            if s[i] in temp:
                temp.remove(s[i])
                for j in range(i, len(s)):
                    res += s[j]
                    if s[j] in temp and len(temp) != 0:
                        temp.remove(s[j])
                    if len(temp) == 0:
                        break
                flag = False
                if len(output) == 0:
                    output = res
                else:
                    if len(output) > len(res) and len(temp)==0:
                        output = res
        return output 

if __name__ == "__main__":
    s = "OUZODYXAZV"
    t = "XYZ"
    solution = Solution()
    print(f"Ouptut is: {solution.minWindow(s, t)}")