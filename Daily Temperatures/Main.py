from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        stack.append(0)

        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures(stack[-1]):
                popped = stack.pop()
                output.append(i - popped)
            stack.append(temperatures[i])
        return output

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    solution = Solution()
    print(f"Output is: {solution.dailyTemperatures(temperatures=temperatures)}")

        