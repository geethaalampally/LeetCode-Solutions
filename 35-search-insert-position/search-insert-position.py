class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        ans=len(nums)
        while left <= right:
            mid = (left + right) // 2

            # if nums[mid] == target:
            #     return mid

            # elif nums[mid] < target:
            #     left = mid + 1

            # else:
            #     right = mid - 1
            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else:
                left=mid+1

        return ans 

        # same concept in longest increasing sub sequence 
        # where the tail value is updated 
        # place of insertion of an element 