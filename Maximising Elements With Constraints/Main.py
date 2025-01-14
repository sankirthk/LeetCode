def getSum(n, value, k):
    count = 0
    if value > k:
        count+=((k+1)*(value+value-k))//2
    else:
        count+=(value*(value+1))//2 + k - value + 1
    
    if value >= n - k:
        count += (value + value - n + 1 + k) * (n - k) // 2
    else:
        count += (value + 1) * value // 2 + n - k - value
    return count - value 
        
def maxElement(n, maxSum, k):
    # Write your code here
    pass
    left, right = 1, maxSum
    while left < right:
        median = (left + right + 1) //2
        result = getSum(n, median, k)
        if result <= maxSum:
            left = median
        else:
            right = median - 1
    
    return left

if __name__ == '__main__':

    length = 522
    maxSum = 685
    index = 395
    output = maxElement(length, maxSum, index)
    print(output)