
class Solution:
    def searchInsert(self, nums, target):
        head = 0
        tail = len(nums) - 1
        if tail < 0: return 0
        while tail >= head:
            middle = head + int((tail - head) / 2)
            if nums[middle] == target:
                return middle

            if target < nums[middle]:
                tail = middle - 1
            else:
                head = middle + 1
        return head

s = Solution()

assert s.searchInsert([1,2,3,4,5,6,7], 7) == 6, "Should be 6"
assert s.searchInsert([1,2,3,4,5,6,7], 1) == 0, "Should be 0"
assert s.searchInsert([], 7) == 0, "Should be 0"

assert s.searchInsert([1,3,5,6], 7) == 4, "Should be 4"
assert s.searchInsert([1,3,5,6], 5) == 2, "Should be 2"
assert s.searchInsert([1,3,5,6], 2) == 1, "Should be 1"
assert s.searchInsert([1,3,5,6], 0) == 0, "Should be 0"
