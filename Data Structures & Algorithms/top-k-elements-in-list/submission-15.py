class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            buckets[cnt].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            res += buckets[i]
            if len(res) == k:
                return res
