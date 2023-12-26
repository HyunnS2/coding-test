def solution1(numbers):
    answer = set([i for i in range(10)]) - set(numbers)
    return sum(answer)


def solution(numbers):
    answer = 0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer