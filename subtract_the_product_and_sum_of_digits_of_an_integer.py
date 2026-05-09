class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        addition=0
        temp=n
        while temp>0:
            rem=temp%10
            product=product*rem
            addition=addition+rem
            temp=temp//10
        return product-addition
