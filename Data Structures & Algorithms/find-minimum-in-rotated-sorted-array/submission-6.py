class Solution:
    def findMin(self, nums: List[int]) -> int:
         l, r = 0, len(nums)-1
         
         while l <= r:
            m = (l+r)//2

            if nums[m] > nums[r]: 
                # right half
                if nums[m+1] > nums[m]:
                    l = m+1
                else:
                    return nums[m+1]
            else:
                # left half inclusive m
                if nums[m] >= nums[l]:
                    r = m-1
                else:
                    l += 1

    
         return nums[l]