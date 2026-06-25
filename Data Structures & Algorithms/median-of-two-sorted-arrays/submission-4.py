class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A, B = nums1, nums2

        total = len(nums1) + len(nums2)
        half = total //2

        l, r = 0, len(A)-1

        
        while True:
            i = (l+r)//2
            j = half - i - 2

            A_l = A[i] if i >= 0 else float("-inf")
            A_r = A[i+1] if i+1 < len(A) else float("inf")
            B_l = B[j] if j >= 0 else float("-inf")
            B_r = B[j+1] if j+1 < len(B) else float("inf")            


            if A_l > B_r: 
                r = i-1
            elif B_l > A_r:
                l = i + 1
            # are we having the correct split
            #if A_l <= B_r and B_l <= A_r:
            else:
                # get Median

                if total%2:
                    # uneven 
                    return min(A_r, B_r)
                else:
                    return (max(A_l, B_l) + min(A_r, B_r)) / 2


            


