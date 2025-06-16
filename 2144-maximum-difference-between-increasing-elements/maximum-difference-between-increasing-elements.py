class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n,ans=len(nums),-inf
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    ans=max(ans,nums[j]-nums[i])
        return -1 if ans==-inf else ans