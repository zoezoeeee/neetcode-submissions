class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isWorks(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            return hours <= h

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2

            if isWorks(mid):
                r = mid
            else:
                l = mid + 1

        return l
