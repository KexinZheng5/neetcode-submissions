class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        
        mid = (len(A) + len(B)) // 2
        l, r = 0, len(A) - 1

        while True:
            ma = (l + r) // 2
            mb = mid - ma - 2

            la = A[ma] if ma >= 0 else float("-infinity")
            ra = A[ma + 1] if (ma + 1) < len(A) else float("infinity")
            lb = B[mb] if mb >= 0 else float("-infinity")
            rb = B[mb + 1] if (mb + 1) < len(B) else float("infinity")

            if la <= rb and lb <= ra:
                if (len(A) + len(B)) % 2:
                    return min(ra, rb)
                return (max(la, lb) + min(ra, rb)) / 2
            elif la > rb:
                r = ma - 1
            else:
                l = ma + 1