class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.mergeSort(points, 0, len(points) - 1)
        print(points)
        ret = points[0:k]
        return ret
    
    def mergeSort(self, arr:  List[List[int]], s: int, e: int):
        if (e - s + 1) <= 1:
            return arr

        m = (e + s) // 2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)

        self.merge(arr, s, m, e)

    def merge(self, arr:  List[List[int]], s: int, m: int,  e: int) -> List[List[int]]:
        ret = []
        l = s
        r = m + 1
        print(f"m: {m}, arr: {arr[s:e+1]}\n")
        while l <= m and r <= e:
            ld = (arr[l][0]**2 + arr[l][1]**2) ** 0.5
            rd = (arr[r][0]**2 + arr[r][1]**2) ** 0.5
            if ld <= rd:
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
        