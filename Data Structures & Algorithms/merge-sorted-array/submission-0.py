class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = two = main = 0
        temp = nums1[0:m]
        while one < m and two < n:
            if temp[one] <= nums2[two]:
                nums1[main] = temp[one]
                one += 1
            else:
                nums1[main] = nums2[two]
                two += 1
            main += 1
        if one == m:
            nums1[main:] = nums2[two:]
        elif two == n:
            nums1[main:] = temp[one:]



'''
nums1 = [5,6,8,40,0,0], m = 4, nums2 = [6,8], n = 2
temp = [5,20,30,40]
main = 3
one = 1
two = 2

ret = [5,6,8,20,30,40]
'''            
        