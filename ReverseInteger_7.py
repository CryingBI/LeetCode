
def reverse(x):
    sum = 0
    sign = 1
    if x < 0:
        x = x*-1
        sign = -1
    while x>0:
        y = x%10
        sum = sum*10 + y
        x = x//10
    if not -2147483648 <= sum <= 2147483647:
        return 0
    return sum * sign

print(reverse(-143))