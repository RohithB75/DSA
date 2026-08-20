class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=1
        o=0
        k=1
        while c < len(nums):
            if nums[c]==nums[c-1]:
                c+=1
                continue
            else:
                nums[o+1]=nums[c]
                o+=1
                k+=1
                c+=1
        return k

        