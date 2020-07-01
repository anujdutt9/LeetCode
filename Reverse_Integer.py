# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            a = int(str(x)[::-1])
        elif x <= 0:
            a = -1 * int(str(x * -1)[::-1])
        
        mina = -2**31  
        maxa = 2**31 - 1  
        
        if a not in range(mina, maxa):  
            return 0  
        else:  
            return a
