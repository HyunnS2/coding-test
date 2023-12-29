
def solution(array):
    
    while len(array) != 0:
        
        # set 함수 = 중복 제거
        # enumerate = 인덱스 리스트 제공
        
        for i, a in enumerate(set(array)):
            array.remove(a)
            
        if i == 0: return a
    
    return -1