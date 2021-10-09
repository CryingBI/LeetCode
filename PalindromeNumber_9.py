def isPalindromeNumber(x) -> bool:
    if x<0:
        return False
    sum = 0
    a = x
    while x>0:
        y = x%10
        sum = sum*10+ y
        x = x//10
    if a == sum: return True
    else: return False


print(isPalindromeNumber(-121))