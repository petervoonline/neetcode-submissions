# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if (e - s + 1) <= 1:
            return 
        
        #Partition
        pivot = arr[e]
        p1 = s - 1
        p2 = s
        while p2 <= e:
            if arr[p2].key < pivot.key:
                p1 += 1
                arr[p1], arr[p2] = arr[p2], arr[p1]
            p2 += 1
        # swap the boundary pointer and the pivot
        arr[e], arr[p1 + 1] = arr[p1 + 1], arr[e]
        

        # divide and conquer
        self.quickSortHelper(arr, s, p1)
        self.quickSortHelper(arr, p1 + 2, e)