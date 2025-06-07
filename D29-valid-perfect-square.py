
# leetcode 367. Valid Perfect Square - https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num>1:
            left,right = 1, num
            
            while left<=right:
                mid = ( left+right )// 2
                if mid*mid > num :
                    right = mid-1
                elif mid * mid < num:
                    left = mid+1
                else:
                    return True
            return False
        elif num==1:
            return True
        else:
            return False

        
        