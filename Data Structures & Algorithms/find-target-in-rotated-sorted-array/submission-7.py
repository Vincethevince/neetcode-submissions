class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # first find the 2 halfs by finding the minimum index
        while l < r:
            m = (l+r)//2

            if nums[m] >= nums[r]:
                l = m+1
            else:
                r = m
        
        min_idx = l
        
        def binary_search(l, r):
            

            while l <= r:
                m = (l+r)//2

                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
        
        if nums[min_idx] <= target <= nums[len(nums)-1]:
            return binary_search(min_idx,len(nums)-1)
        else:
            return binary_search(0, min_idx-1)


    
