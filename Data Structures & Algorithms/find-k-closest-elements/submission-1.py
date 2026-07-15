class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) -1
        res = []
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>=x:
                r = mid - 1
            else:
                l = mid + 1
        
        l,r = r,l
        while k > 0:
            if l<0:
                res.append(arr[r])
                r+=1
            elif r >= len(arr):
                res.insert(0, arr[l])
                l-=1
            elif r < len(arr) and abs(arr[r] - x) < abs(arr[l]-x):
                res.append(arr[r])
                r+=1
            elif (l >= 0 and abs(arr[l] - x) <= abs(arr[r]-x)):
                res.insert(0, arr[l])
                l-=1
            k-=1
            
        
        return res



        