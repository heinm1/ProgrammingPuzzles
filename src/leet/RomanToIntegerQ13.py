class Solution:

    romanNumerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:

        baseTenResult = 0
        index = 0

        while index < len(s):

            inspecting = self.romanNumerals[s[index]]
            next = 4000 if index == len(s)-1 else self.romanNumerals[s[index+1]]

            if inspecting < next and next < 4000:
                baseTenResult = baseTenResult - inspecting + next
                index = index + 1
            else:
                baseTenResult = baseTenResult + inspecting

            index = index + 1

        return baseTenResult


s = Solution()
assert s.romanToInt("III") == 3, "Should be 3"
assert s.romanToInt("IV") == 4, "Should be 4"
assert s.romanToInt("IX") == 9, "Should be 9"
assert s.romanToInt("LVIII") == 58, "Should be 58"
assert s.romanToInt("MCMXCIV") == 1994, "Should be 1994"
assert s.romanToInt("MMMCMXCIX") == 3999, "Should be 3999"