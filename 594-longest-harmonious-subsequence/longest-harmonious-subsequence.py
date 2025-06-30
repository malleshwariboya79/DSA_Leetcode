class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 1
        ans = 0

        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 2 if nums[1] - nums[0] == 1 else 0

        while j < len(nums):
            if nums[j] - nums[i] == 1:
                ans = max(ans, j - i + 1)
                j += 1
            elif nums[j] - nums[i] > 1:
                i += 1
            else:
                j += 1

        return ans