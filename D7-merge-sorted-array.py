from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = nums1[:len(nums1)-n]+nums2
        t.sort()
        for i in range(len(t)):
            nums1[i] = t[i]
        for i,j in zip(nums1,range(len(nums1)-1)):
            if (i==0) and (nums1[j+1]<0):
                nums1.remove(0)


s= Solution()
print(s.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3))