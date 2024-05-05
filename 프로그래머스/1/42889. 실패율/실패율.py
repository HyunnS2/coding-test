def solution(N, stages):
    
    answer = []
    dic = {}
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count/length
        
        length -= count
        dic[i] = fail
        
    S = sorted(dic.items() , key = lambda x :x[1], reverse=True)
    S = dict(S)
    answer = list(S.keys())
    
    
    return answer