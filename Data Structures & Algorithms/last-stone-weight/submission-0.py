class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            next_largest = -heapq.heappop(max_heap)

            if largest != next_largest:
                heapq.heappush(max_heap, next_largest - largest)

        return -max_heap[0] if max_heap else 0
         