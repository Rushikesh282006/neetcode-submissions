class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [(-1 * s) for s in stones]

        heapq.heapify(heap)

        while len(heap) != 1:
            max_num = heapq.heappop(heap) * -1
            second_max_num = heapq.heappop(heap) * -1

            heapq.heappush(heap,(max_num-second_max_num)*-1)

        
        return heap[0]*-1

