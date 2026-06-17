class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}
        for i in range(len(nums)):
            mappings[nums[i]] = i
        
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in mappings:
                if mappings[diff] != i:
                    return [i, mappings[diff]]

        return None