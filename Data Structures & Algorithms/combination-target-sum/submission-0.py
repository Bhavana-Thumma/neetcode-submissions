class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(nums)):
                if(nums[i] > remaining):
                    break
                path.append(nums[i])
                backtrack(i, remaining - nums[i], path)
                path.pop()
        nums.sort()
        backtrack(0, target, [])
        return result
