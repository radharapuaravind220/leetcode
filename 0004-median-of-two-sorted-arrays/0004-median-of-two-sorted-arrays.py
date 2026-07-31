class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        total=m+n
        i=0
        j=0
        cur=prev=0
        for _ in range(total//2+1):
            prev=cur
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    cur=nums1[i]
                    i+=1
                else:
                    cur=nums2[j]
                    j+=1
            elif i<m:
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        return cur if (total & 1)==1 else (cur+prev)/2