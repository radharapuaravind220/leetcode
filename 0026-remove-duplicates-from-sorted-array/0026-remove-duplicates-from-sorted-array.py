class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        n=len(nums)
        if n==1:
            return 1
        while j<n:
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return i+1