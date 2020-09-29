def get_max_profit(arr):
    '''
    121. Best Time to Buy and Sell Stock

        Say you have an array for which the ith element is the 
    price of a given stock on day i.
        If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock), design an algorithm 
    to find the maximum profit.
        Note that you cannot sell a stock before you buy one.
    '''
    if not arr:
        return 0
    min_so_far = float('inf')
    max_profit = 0
    for val in arr:
        min_so_far = min(min_so_far, val)
        max_profit = max(max_profit, val - min_so_far)
    return max_profit

if __name__ == "__main__":
    test1 = [310,315,275,295,260,270,290,230,255,250]
    print(get_max_profit(test1))