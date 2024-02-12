'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
Use Binary Search to get the closest position
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lptr = 0
        rptr = len(nums)-1
        closest = 0
        while lptr<=rptr:
            mid = (lptr + rptr)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                rptr = mid-1
            else:
                lptr = mid+1
                closest = lptr
        return closest
