class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)-1):
            seen=set()
            for j in range(i+1, len(nums)):
                th = -(nums[i]+nums[j])
                if(th in seen):
                    triplet = tuple(sorted([nums[i], nums[j], th]))
                    result.add(triplet)
                seen.add(nums[j])
        print([list[x] for x in result])
        return [list(x) for x in result]
