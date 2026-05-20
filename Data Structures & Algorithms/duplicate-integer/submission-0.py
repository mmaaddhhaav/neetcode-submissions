class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hah = {}
        for num in nums:
            if num in hah:
                return True   # duplicate found
            hah[num] = 1
        return False