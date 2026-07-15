class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap={}
        l=0
        count=0
        for r in range(len(fruits)):
            if fruits[r] in hashmap:
                hashmap[fruits[r]]+=1
            else:
                hashmap[fruits[r]]=1
            while len(hashmap)>2:
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]]==0:
                    del hashmap[fruits[l]]
                l+=1
            count=max(count,r-l+1)
        return count
