class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp=n
            prod=1
            while temp:
                r=temp%10
                prod*=r
                temp=temp//10
            if prod%t==0:
                return n
            else:
                n+=1
