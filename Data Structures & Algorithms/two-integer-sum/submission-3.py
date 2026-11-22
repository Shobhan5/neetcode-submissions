class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = None
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    l = list((i,j))
        return l

        