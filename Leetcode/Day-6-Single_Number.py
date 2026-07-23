class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans

        # hashmap={}
        # for i in nums:
        #     hashmap[i]=hashmap.get(i,0)+1
        # for key,value in hashmap.items():
        #     if value==1:
        #         return key


        # hashmap = {}

        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1

        # for key, value in hashmap.items():
        #     if value == 1:
        #         return key
       
       
        # for i in nums:
        #     count=0
        #     for j in nums:
        #         if j==i:
        #             count+=1
        #     if count==1:
        #         return i


# XOR Basics
#The one thing to memorize
# Whenever you see XOR, remember these three rules:


# a ^ a = 0     # same numbers disappear

# a ^ 0 = a     # zero changes nothing

# XOR works bit by bit
# Everything else follows from these rules.

