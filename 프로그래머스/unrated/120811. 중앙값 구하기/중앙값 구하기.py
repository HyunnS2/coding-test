def solution2(array):
    array.sort()
    m = len(array)//2
    return array[m]


def solution(array):
    answer = 0
    array.sort()
    length = len(array)
    m = int(length/2)
    answer = array[m]
    return answer