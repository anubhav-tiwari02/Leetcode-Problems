class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_num = []
        for digit in str(n):
            if digit != '0':
                new_num.append(digit)
        if not new_num:
            return 0
        x = int("".join(new_num))
        s = sum(int(d) for d in new_num)
        return x * s
