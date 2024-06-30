class Solution:
    def isPalindrome(self, x: int):
        n=x
        rev=0
        while x >0:
            digit=x%10
            rev=rev*10+digit
            x//=10
        if rev == n:
            return "true"
        else:
            return "false"
x=int(input())
r=Solution()
print(r.isPalindrome(x))

