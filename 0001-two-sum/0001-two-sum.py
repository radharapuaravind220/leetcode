class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        d={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in d:
                return d[s],i
            else:
                d[nums[i]]=i
        return -1
            