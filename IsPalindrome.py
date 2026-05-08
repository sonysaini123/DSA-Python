class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse=0
        if temp<0:
            return False
        while temp>0:
            rem=temp%10
            temp//=10
            reverse=(reverse*10)+rem
        return reverse==x

#short method- using by string
       
        #return str(x)==str(x)[::-1]
