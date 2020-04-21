
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) == 0: return ""
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for w in range(1, len(strs)):
                if i >= len(strs[w]) or strs[w][i] != c:
                    return strs[0][0:i]
        return strs[0]

s = Solution()
assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl", "Should be fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == "", "Should be empty"
assert s.longestCommonPrefix(["racecar","racecar","racecar"]) == "racecar", "Should be racecar"
assert s.longestCommonPrefix([]) == "", "Should be empty"
assert s.longestCommonPrefix(None) == "", "Should be empty"
assert s.longestCommonPrefix(["","",""]) == "", "Should be empty"
assert s.longestCommonPrefix(["fl","flow","flower"]) == "fl", "Should be fl"
assert s.longestCommonPrefix(["flower","flow","fl"]) == "fl", "Should be fl"
