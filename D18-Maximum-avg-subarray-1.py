"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

Leetcode - https://leetcode.com/problems/maximum-average-subarray-i/
"""



"""
Why this works
1. You’re looking for the maximum average of a contiguous subarray of length k.
2. You can calculate the average by summing the elements of the subarray and dividing by k.
3. You can use a sliding window approach to efficiently calculate the sum of each subarray of length k.
4. Initialize a variable to keep track of the maximum average found so far.
5. Iterate through the array, updating the sum of the current subarray by adding the new element and removing the old one.
6. Update the maximum average if the current average is greater than the maximum found so far.
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize max_avg with negative infinity to ensure any real average will be higher
        max_avg = float('-inf')

        # Calculate the sum of the first 'k' elements (first window)
        current_sum = sum(nums[:k])
        # Compute the average of the first window and store it as the initial max
        max_avg = current_sum / k

        # Start sliding the window from the (k)th element to the end of the array
        for i in range(k, len(nums)):
            # Add the new element entering the window and subtract the one leaving
            current_sum += nums[i] - nums[i - k]
            # Compute the new average
            temp_avg = current_sum / k
            # Update max_avg if the new average is higher
            if temp_avg > max_avg:
                max_avg = temp_avg

        # Return the highest average found
        return max_avg


"""

This solution solves 95% usecases but is not optimal for all cases.
The time complexity is O(n*k) because for each of the n-k+1 subarrays, we are calculating the sum of k elements. This can be improved to O(n) using a sliding window approach.


Intuition
1. You’re looking for the maximum average of a contiguous subarray of length k.
2. You can calculate the average by summing the elements of the subarray and dividing by k.
3. You can use a sliding window approach to efficiently calculate the sum of each subarray of length k.
4. Initialize a variable to keep track of the maximum average found so far.
5. Iterate through the array, updating the sum of the current subarray by adding the new element and removing the old one.
6. Update the maximum average if the current average is greater than the maximum found so far.

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):  # Stop when i+k would exceed len(nums)
            temp_avg = sum(nums[i:i+k]) / k
            if temp_avg >= max_avg:
                max_avg = temp_avg
        return max_avg
# Test the function
if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(f"The maximum average of the subarray of length {k} is: {result:.5f}")
    # Output: 12.75000
   """ 