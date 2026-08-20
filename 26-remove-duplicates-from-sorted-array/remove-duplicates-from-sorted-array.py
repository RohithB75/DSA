class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cm=1
        officier=0
        k=1
        while cm < len(nums):
            if nums[cm]==nums[cm-1]:
                cm+=1
                continue
            else:
                nums[officier+1]=nums[cm]
                officier+=1
                k+=1
                cm+=1
        return k

        