#Find if the given number is a perfect square of some other number.
#For eg: if input=16, return True. Whereas if input=14, return False.
#Use binary search with time complexity of O(log n) to search for the square root of the number.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lptr = 0
        rptr = num
        while lptr<=rptr:
            mid = lptr + (rptr-lptr)//2
            square = mid**2
            if square>num:
                rptr = mid-1
            elif square<num: 
                lptr = mid + 1
            else:
                return True
        return False
