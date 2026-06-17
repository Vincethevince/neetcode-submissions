class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # always add larger ones and pop if new one is smaller than top
        stack = []
        maxA = 0
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][0] > h:
                old_height,last_i = stack.pop()
                maxA = max(maxA, (i-last_i)*old_height)
                index = last_i

            stack.append((h, index))
        
        for h,i in stack:
            maxA = max(maxA, (len(heights)-i)*h)

        return maxA

