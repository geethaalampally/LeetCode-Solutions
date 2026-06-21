from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Possible majority candidates
        cand1 = cand2 = None
        count1 = count2 = 0

        # Boyer-Moore Voting Algorithm
        for num in nums:

            if cand1 == num:
                count1 += 1

            elif cand2 == num:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1

            elif count2 == 0:
                cand2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Verify the candidates
        ans = []

        for cand in {cand1, cand2}:
            if nums.count(cand) > len(nums) // 3:
                ans.append(cand)

        return ans