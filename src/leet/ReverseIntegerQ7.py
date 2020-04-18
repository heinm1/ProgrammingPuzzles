class Solution:
    def reverse(self, x: int) -> int:
        normalisation = -1 if x < 0 else 1
        x = x * normalisation
        reversed = 0
        while x > 0:
            if reversed > (2**31)/10 or (reversed == (2**31)/10 and x%10 > 7): return 0
            reversed = reversed * 10 + x%10
            x = int(x/10)
        return reversed * normalisation

    def reverse2(self, x: int) -> int:
        return int(str(x)[::-1]) if x >= 0 else int(str(x*-1)[::-1])*-1

s = Solution()
print(s.reverse(123456789))