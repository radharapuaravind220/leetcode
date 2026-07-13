class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==1:
            pass
        else:
            for i in range(0,n-1):
                
                for j in range(i+1,n):
                    if nums[i]>=nums[j]:
                        nums[i],nums[j]=nums[j],nums[i]
            
        