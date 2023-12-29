def solution2(n):
    answer = 0
    
    for i in range(0,n+1):
        if i%2==0:
            answer += i
    
    return answer

def solution3(n):
    answer = [i for i in range(0,n+1) if i%2==0]
    return sum(answer)

def solution(n):
    answer = [i for i in range(0,n+1, 2) ]
    return sum(answer)