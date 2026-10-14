class Solution(object):
    def maxSumOfSquares(self, num, sum):
        number=(num,sum)
        if sum>9*num or sum<0:
            return ""
        digits=[]
        for i in range(num):
            digit=min(9,sum)
            digits.append(str(digit))
            sum-=digit
        if sum!=0:
            return ""
        return "".join(digits)
        