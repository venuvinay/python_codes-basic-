class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        v=[]
        v.extend(nums1)
        v.extend(nums2)
        v.sort()
        n=len(v)
        if n%2==0:
            m=v[int(n/2)-1]+v[int((n/2))]
            print(m/2)
        else:
            print(v[n//2])
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
a=Solution()
a.findMedianSortedArrays(num1,num2)
        
