class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        A = nums1
        B = nums2
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l = 0
        r = len(A) - 1

        while True:
            m = (l+r)//2
            m2 = half - m - 2

            Aleft = A[m] if m >= 0 else float("-inf")
            Aright = A[m+1] if (m+1) < len(A) else float("inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")
            Bright = B[m2+1] if (m2+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Bright, Aright)
                else:
                    maxLeft = max(Aleft, Bleft)
                    minRight = min(Aright, Bright)
                    return float(maxLeft + minRight) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1




            