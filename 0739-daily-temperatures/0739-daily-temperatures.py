class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        l=len(arr)
        nge=[0]*l
        st=[]
        for i in range(l-1,-1,-1):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if st:
               nge[i]=st[-1]-i 
            st.append(i)
        return nge