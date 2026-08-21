class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        res=[0]*(m+n)
        k=0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                res[k]=nums1[i]
                k+=1
                i+=1
            else:
                res[k]=nums2[j]
                k+=1
                j+=1
        while j<n:
            res[k]=nums2[j]
            k+=1
            j+=1

        while i<m:
            res[k]=nums1[i]
            k+=1
            i+=1
        nums1[:]=res