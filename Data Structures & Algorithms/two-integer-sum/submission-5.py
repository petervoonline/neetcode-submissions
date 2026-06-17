class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}            
        
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in mappings:
                return [mappings[diff], i]
            mappings[nums[i]] = i
