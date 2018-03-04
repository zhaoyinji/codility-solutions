def solution(A):
    max_profit = 0
    min_buy = 200000
    
    for buy in A:
            min_buy = min(buy, min_buy)
            max_profit = max(max_profit, buy - min_buy)
    
    return max_profit