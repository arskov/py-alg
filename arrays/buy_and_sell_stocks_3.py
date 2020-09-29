def get_max_profit(arr):
    '''
    123. Best Time to Buy and Sell Stock III
    
        Say you have an array for which the ith element is the price of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete at most two transactions.
        Note: You may not engage in multiple transactions at the same time 
    (i.e., you must sell the stock before you buy again).
    '''
    if not arr:
        return 0
    l = len(arr)
    min_so_far = float('inf')
    max_profit = 0
    max_profit_arr =[0] * l
    for i in range(l):
        min_so_far = min(min_so_far, arr[i])
        max_profit = max(max_profit, arr[i] - min_so_far)
        max_profit_arr[i] = max_profit
    max_so_far = float('-inf')
    max_profit = 0
    total_max = 0
    for i in range(l - 1, 0, -1):
        max_profit = max(max_profit, max_so_far - arr[i])
        max_so_far = max(max_so_far, arr[i])
        total_max = max(total_max, max_profit + max_profit_arr[i])
    return total_max


if __name__ == "__main__":
    test1 = [310,315,275,295,260,270,290,230,255,250]
    print(get_max_profit(test1))
    test2 = [12,11,13,9,12,8,14,13,15]
    print(get_max_profit(test2))
    test3 = [1,2,3,4,5]
    print(get_max_profit(test3))