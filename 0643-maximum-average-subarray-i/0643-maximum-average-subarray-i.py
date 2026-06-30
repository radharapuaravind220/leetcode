class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window=sum(nums[:k])

        max1=window
        for i in range(len(nums)-k):
            window=window-nums[i]+nums[i+k]
            max1=max(window,max1)
        return max1/k

