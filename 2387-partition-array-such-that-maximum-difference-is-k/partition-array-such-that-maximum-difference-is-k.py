class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count=0 
        n=len(nums)
        i=0
        while i<n:
            count+=1
            start=nums[i]
            while i<n and nums[i]-start<=k:
                i+=1
        return count


    

        