def find_triplet_sum():
    nums=[0,0,0]
    target=0
    n=len(nums)
    nums.sort()
    for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        s=nums[i]+nums[j]+nums[k]
                        if s==target:
                              print(s)

find_triplet_sum()


