def solution(n, k):
    
    food = n * 12000
    
    if n >= 10:
        juice = (k * 2000) - (n//10 * 2000)
    else:
        juice = k * 2000
    
    answer = food + juice
    
    return answer