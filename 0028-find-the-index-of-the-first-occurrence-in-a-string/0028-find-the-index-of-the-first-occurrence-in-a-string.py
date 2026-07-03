class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack.split(needle)
        if needle in haystack:
            return haystack.index(needle)
        return -1