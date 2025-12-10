nums = [1,2,4,6]

l1 = [1] * len(nums)
l2 = [1] * len(nums)
ans = 1

for i in range(1,len(nums)):
  ans *= nums[i-1]
  l1[i] = ans
print(l1)
ans = 1
for i in range(len(nums)-2,-1,-1):
  ans *= nums[i+1]
  l2[i] = ans

print(l2)
print(l2)
l = []
for i in range(0,len(l1)):
  l.append(l1[i]*l2[i])

print(l)