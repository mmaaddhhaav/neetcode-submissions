class Solution:
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        elif index >= len(nums):
            return
        sum_i = total + nums[index]
        subset.append(nums[index])
        self.solve(index, sum_i, subset, nums, target, result)
        sum_i = total
        subset.pop()
        self.solve(index+1, sum_i, subset, nums, target, result)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result