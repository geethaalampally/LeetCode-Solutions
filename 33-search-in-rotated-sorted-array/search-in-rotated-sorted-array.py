class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx=-1
        for i in range(len(nums)):
            if nums[i]==target:
                idx=i
                break
        return idx