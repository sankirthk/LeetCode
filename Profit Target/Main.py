def stockPairs(stocksProfit, target):
    # Set to track seen elements and pairs
    seen = set()
    pairs = set()
    
    for profit in stocksProfit:
        complement = target - profit
        
        # If the complement is in seen and not already added to pairs
        if complement in seen and (profit, complement) not in pairs and (complement, profit) not in pairs:
            pairs.add((profit, complement))
        seen.add(profit)
    
    # The result is the number of unique pairs
    return len(pairs)
    
    
if __name__ == '__main__':

    input1 = [6,12,3,9,3,5,1]
    target = 12
    output = stockPairs(input1, target)
    print(output)