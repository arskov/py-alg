def get_max_profit(arr):
    '''
    122. Best Time to Buy and Sell Stock II
    
        Say you have an array prices for which the ith element is the price
    of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete as
    many transactions as you like (i.e., buy one and sell one share of 
    the stock multiple times).
        Note: You may not engage in multiple transactions at the same time
    (i.e., you must sell the stock before you buy again).
    '''
    if not arr:
        return 0
    max_profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_profit += arr[i] - arr[i - 1]
    return max_profit

if __name__ == "__main__":
    test1 = [310,315,275,295,260,270,290,230,255,250]
    print(get_max_profit(test1))
    test2 = [7,1,5,3,6,4]
    print(get_max_profit(test2))