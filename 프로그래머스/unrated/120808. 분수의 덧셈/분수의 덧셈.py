import math

def solution(denom1, num1, denom2, num2):
    
    boonmo = num1 * num2
    boonja = denom1 * num2 + denom2 * num1
    
    gcd_value = math.gcd(boonmo,boonja)
    
    answer = [boonja/gcd_value, boonmo/gcd_value]
    
    return answer



