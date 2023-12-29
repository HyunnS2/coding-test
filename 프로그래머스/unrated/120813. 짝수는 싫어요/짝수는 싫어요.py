def solution2(n):
    answer = []
    for i in range(1,n+1):
        if i%2!=0:
            answer.append(i)
    return answer

def solution3(n):
    answer = []
    for i in range(1,n+1, 2):
        answer.append(i)
    return answer


def solution(n):
    return [i for i in range(1,n+1, 2)]


