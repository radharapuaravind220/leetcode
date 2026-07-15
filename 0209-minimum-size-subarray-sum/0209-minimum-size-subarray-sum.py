class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """minl=float('inf')
        sum1,l,r=0,0,0
        n=len(nums)
        while r<n:
            while l<=r and sum1>target:
                sum1-=nums[l]
                l-=1
            if sum1==target:
                minl=min(minl,r-l)
            r+=1
            if r<n:
                sum1+=nums[r]
        return 0 if minl==float('inf') else minl """
        l=0
        sum1=0
        mini=float('inf')
        for r in range(len(nums)):
            sum1+=nums[r]
            while sum1>=target:
                mini=min(mini,r-l+1)
                sum1-=nums[l]
                l+=1
            
                
        return 0 if mini==float('inf') else mini