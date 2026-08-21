class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        p = 0
        q = 0
        
        for i in range(len(nums)):
            if i==0 or nums[i-1]!=nums[i]:
                p = 1
            else:
                p += 1
            
            if p<=k:
                nums[q] = nums[i]
                q +=1
        
        return nums[:q]