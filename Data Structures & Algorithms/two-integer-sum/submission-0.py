class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums) - 1
        for i in range(len(nums) - 1):
            j = i + 1
            while j <= len(nums) - 1:
                if nums[j] + nums[i] == target:
                    return [i, j]
                j += 1
        return nums