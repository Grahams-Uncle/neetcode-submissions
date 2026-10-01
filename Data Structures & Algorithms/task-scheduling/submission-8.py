class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        time = 0
        cooldown = deque() # [available_time, -remaining_frequency]

        while heap or cooldown:
            if cooldown and cooldown[0][0] <= time:
                ready_time, freq = cooldown.popleft()
                heapq.heappush(heap, freq)
            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq < 0:
                    cooldown.append((time + n + 1, freq))
            time += 1
        return time