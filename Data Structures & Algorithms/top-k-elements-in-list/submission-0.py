class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1   # Step 1: count
        
        # Step 2: sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: take top k
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res
