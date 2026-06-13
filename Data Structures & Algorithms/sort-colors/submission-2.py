class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = mid = 0
        hi = len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1
            else:
                mid += 1
        

        