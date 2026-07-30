class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            new_list = [int(digit) for digit in str(num)]
            new_num = []
            while new_list:
                min_int = min(new_list)
                new_num.append(min_int)
                new_list.remove(min_int)
            for i in range(len(new_num)):
                if new_num[i] != 0:
                    new_num[0], new_num[i] = new_num[i], new_num[0]
                    break
            return int("".join(map(str, new_num))) if new_num else 0
        else:
            new_list = [int(digit) for digit in str(-num)]
            new_num = []
            while new_list:
                max_int = max(new_list)
                new_num.append(max_int)
                new_list.remove(max_int)
            return -int("".join(map(str, new_num)))