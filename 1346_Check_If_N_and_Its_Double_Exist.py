#sort array
#keep double value as target
#binary search
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        for i in range(len(arr)):
            target = arr[i]*2 
            lptr = 0
            rptr = len(arr)-1
            while lptr<=rptr:
                mid = (lptr + rptr)//2
                if (arr[mid]==target) and (mid!=i):
                    return True
                elif arr[mid]>target:
                    rptr = mid-1
                else:
                    lptr = mid+1
        return False
