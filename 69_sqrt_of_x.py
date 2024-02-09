#Find the square root of a number using binary search
#when <x, update the closest point as we need to find a number <=square root of x
class Solution:
    def mySqrt(self, x: int) -> int:
        lptr = 0
        rptr = x
        closest = 0
        while lptr<=rptr:
            mid = (lptr + rptr)//2
            sqrt = mid*mid
            if sqrt>x:
                rptr = mid-1
            elif sqrt<x:
                lptr = mid+1
                closest = mid
            else:
                return mid
        return closest
