class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the dip
        idx = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        # Step 2: If no dip exists
        if idx == -1:
            nums.reverse()

        else:

            # Step 3: Find just greater element
            for i in range(n - 1, idx, -1):
                if nums[i] > nums[idx]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    break

            # Step 4: Reverse suffix
            left = idx + 1
            right = n - 1

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1