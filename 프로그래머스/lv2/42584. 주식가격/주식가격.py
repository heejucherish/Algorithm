def solution(prices):
    answer = [0]* len(prices)
    stack = []
    
    for cur_day, cur_money in enumerate(prices):
        while stack and stack[-1][1] > cur_money:
            pre_day, _ = stack.pop()
            answer[pre_day] = cur_day - pre_day 
        
        stack.append((cur_day, cur_money))
        
    while stack:
        pre_day, _ = stack.pop()
        answer[pre_day] = len(prices) -1 - pre_day
        

        
    return answer