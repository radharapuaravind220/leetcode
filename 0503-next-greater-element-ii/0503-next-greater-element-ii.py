class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        st=[]
        for i in range(n*2-1,-1,-1):
            num=nums[i%n]
            while st and st[-1]<=num:
                st.pop()
            if st and i<n:
                res[i]=st[-1]
            st.append(nums[i%n])
        return res
