class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m - 1
        two = n - 1
        main = m + n - 1
        while two >= 0:
            if one >= 0 and nums1[one] > nums2[two]:
                nums1[main] = nums1[one]
                one -= 1
            else:
                nums1[main] = nums2[two]
                two -= 1
            main -= 1


'''
nums1=[10,20,10,20,20,40]
m=4
nums2=[1,2]
n=2

one -1
two 1
main 1

'''
           
        