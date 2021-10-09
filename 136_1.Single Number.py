
def singleNumber(nums) -> int:
        nums2 = []
        
        for i in nums:
            if i not in nums2:
                nums2.append(i)
            else:
                nums2.remove(i)
            
        return nums2.pop()

def singleNumber2(nums) -> int:
    return 2 * sum(set(nums)) - sum(nums)

def singleNumber3(nums) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a

a = [4,1,2,2,1]
b = singleNumber(a)
c = singleNumber2(a)
d = singleNumber3(a)
print(b)
print(c)
print(d)