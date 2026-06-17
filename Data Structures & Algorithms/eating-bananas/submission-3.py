class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k = float("inf")
        l,r = 1, max(piles)
        while l<=r:
            m = (l+r)//2
            time =self.eatAll(piles,m) 
            if time <= h:
                k = min(k,m)
                r = m - 1
            elif time > h:
                l = m+1

        return k


    def eatAll(self,piles, k):
        time = 0
        for p in piles:
            time += math.ceil(p/k)
        
        return time