class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m - 1
        two = n - 1
        main = m + n -1
        while one >= 0 and two >= 0:
            if nums1[one] <= nums2[two]:
                nums1[main] =  nums2[two]
                two -= 1
            else:
                nums1[main] = nums1[one]
                one -= 1
            main -= 1
        if one < 0:
            nums1[0:main+1] = nums2[0:two+1]
        elif two == n:
            nums1[0:main+1] = nums1[0:one+1]



'''
nums1 = [5,6,8,40,0,0], m = 4, nums2 = [6,8], n = 2
temp = [5,20,30,40]
main = 3
one = 1
two = 2

ret = [5,6,8,20,30,40]
'''            
        