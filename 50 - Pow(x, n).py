class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x,n):
            if n==0:
                return 1
            if n%2==1:
                half = recur(x,((n-1)//2))
                if half > 10**4 or half< -10**4:
                    return min(max(half,-10**4),10**4)
                return x*half*half
            else:
                half = recur(x,n//2)
                if half > 10**4 or half< -10**4:
                    return min(max(half,-10**4),10**4)
                return half*half
        if n >=0:
            return recur(x,abs(n))
        else:
            return recur(1/x,abs(n))
        return recur(x,n)