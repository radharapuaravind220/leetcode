class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res=[]
        for r in range(len(nums)):
            if res:
                res.append(res[-1]+nums[r])
            else:
                res.append(nums[r])
        for r in range(len(nums)):
            
            if res[-1]-res[r]==res[r]-nums[r]:
                return r
        return -1
        