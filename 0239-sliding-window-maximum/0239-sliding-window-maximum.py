from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=len(nums)

        queue= deque()
        for r in range(len(nums)):
            while queue and queue[0]<=r-k:
                queue.popleft()
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)
            if r>=k-1:
                res.append(nums[queue[0]])
        return res
