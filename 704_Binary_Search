class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #complexity O(log n)
        lptr = 0 #initialize left and right pointer to first and last element
        rptr = len(nums)-1
        mid = (lptr + rptr)//2 
        while lptr<=rptr:
            if nums[mid]==target:
                return mid #if the target is the middle element, return the index
            if nums[mid]>target:
                rptr = mid-1  #if the middle element is higher than the target, search in the left half
            else:
                lptr = mid+1   #else search in the right half
            mid = (lptr + rptr)//2
        return -1
