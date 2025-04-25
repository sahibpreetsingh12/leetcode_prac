"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.


https://leetcode.com/problems/remove-element/

"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # this is normal problem using while loop to rmeove all elements
        while val in nums:
            nums.remove(val)
        return len(nums)
    

"""
Anotehr Apporach

1. Initialize index to 0, which represents the current position for the next non-target element.

2. Iterate through each element of the input array using the i pointer.

3. For each element nums[i], check if it is equal to the target value val.

4. If nums[i] is not equal to val, it means it is a non-target element.

5. Set nums[index] = nums[i] to store the non-target element at the current index position.

6. Increment index by 1 to move to the next position for the next non-target element.

7. Continue this process until all elements in the array have been processed.

8. Finally, return the value of index, which represents the length of the modified array.

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index