class Solution:
    def twoSum(self, nums, target):
        l=[]
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] == target:
                l.append(i)
                l.append(i+1)
        print(l)
nums=list(map(int,input().split()))
target=int(input())
r=Solution()
r.twoSum(nums,target)
