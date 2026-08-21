class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0      # write pointer: next slot for a "kept" element
        count = 0  # how many times the current value has been kept

        for j in range(len(nums)):       # read pointer: scans every element
            if i > 0 and nums[i - 1] == nums[j]:
                count += 1                # same value as last kept one
            else:
                count = 1                 # new value → restart count

            if count <= k:
                nums[i] = nums[j]         # keep it: write into the front region
                i += 1                    # only advance i when we keep something

        return nums[:i]