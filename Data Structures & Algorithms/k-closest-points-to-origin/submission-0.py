class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:

            dist_sq = -(x**2 + y**2) 

            if len(heap) == k:
                heapq.heappushpop(heap, (dist_sq, x, y))
            else:
                heapq.heappush(heap, (dist_sq, x, y))
        
        return [[x, y] for (dist_sq, x, y) in heap]