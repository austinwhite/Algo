# Time Complexty: Linear, O(n) where n is the length of nums
# Space Complexty: Linear, 0(n) where n in the length of nums

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(nums)):
            if target-nums[i] in compliments:
                return [compliments[target-nums[i]],i]
            else:
                compliments[nums[i]] = i
