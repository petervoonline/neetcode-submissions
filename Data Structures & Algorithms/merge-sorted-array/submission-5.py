class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        main = m + n - 1
        one = m - 1
        two = n - 1
        while two >= 0:
            if one >= 0 and nums1[one] >= nums2[two]:
                nums1[main] = nums1[one]
                one -= 1
            else:
                nums1[main] = nums2[two]
                two -= 1
            main -= 1


           
        