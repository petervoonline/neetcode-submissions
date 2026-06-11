# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.sort(pairs, 0, len(pairs) - 1)

    def sort(self, arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2
        self.sort(arr, s, m)
        self.sort(arr, m+1, e)

        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> List[Pair]:
        ret = []

        l = s
        r = m + 1

        while l <= m and r <= e:
            if arr[l].key <= arr[r].key:
                ret.append(arr[l])
                l += 1
            else:
                ret.append(arr[r])
                r += 1
        
        if l > m:
            ret.extend(arr[r:e+1])
        else:
            ret.extend(arr[l:m+1])
        
        arr[s:e+1] = ret               

