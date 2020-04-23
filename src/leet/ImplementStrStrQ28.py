class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        for index in range(0, len(haystack)):
            if (len(needle) + index > len(haystack)): return -1
            indexToReturn = index
            for i in range(0, len(needle)):
                if (haystack[index+i] != needle[i]):
                    indexToReturn = -1
                    break
            if indexToReturn != -1: return indexToReturn
        return -1

s = Solution()
assert s.strStr("hello", "") == 0, "Should be 0"
assert s.strStr("hello", "ll") == 2, "Should be 2"
assert s.strStr("aaa", "bba") == -1, "Should be -1"
assert s.strStr("", "bba") == -1, "Should be -1"
assert s.strStr("aaa", "aaaa") == -1, "Should be -1"