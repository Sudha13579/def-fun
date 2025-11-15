
nums = [-1, 2, 1, -4]
target = 1#Output: 2#-1+2++1=2 2+1-4=-1
n=len(nums)
l=0
temp=0
k=3
ans=0
for i in range(n):
    temp+=nums[i]
    if i-l==k:
        temp-=nums[l]
        l+=1
    if i-l+1==k:
        
        
