class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        """if n==1:
            pass
        else:
            for i in range(0,n-1):
                
                for j in range(i+1,n):
                    if nums[i]>=nums[j]:
                        nums[i],nums[j]=nums[j],nums[i]"""
        #dutch national flag algorithm
        low,mid=0,0
        high=n-1
        while mid<=high:
            if nums[mid]==1:
                mid+=1
            elif nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            
        