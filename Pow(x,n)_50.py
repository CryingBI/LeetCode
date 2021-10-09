
def myPow( x: float, n: int) -> float:
        if(n==0): return 1
        if(n==1): return x
        if(n<0): return myPow(1/x,-n)
        result = myPow(x,n//2)
        result *= result
        if(n%2==1): result = result*x
        return result


a = myPow(3,20)
print(a)