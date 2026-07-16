class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.newSub(nums,k) - self.newSub(nums,k-1)
    def newSub(self,nums,k):
        count=0
        dict1={}
        l=0
        for r in range(len(nums)):
            if nums[r]  in dict1:
                dict1[nums[r]]+=1
            else:
                dict1[nums[r]]=1
            while len(dict1)>k:
                dict1[nums[l]]-=1
                if dict1[nums[l]]==0:
                    del  dict1[nums[l]]
                l+=1
            count+=r-l+1
        return count

