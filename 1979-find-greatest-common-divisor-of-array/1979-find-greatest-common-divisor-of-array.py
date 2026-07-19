class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a 
        return gcd(a,b)