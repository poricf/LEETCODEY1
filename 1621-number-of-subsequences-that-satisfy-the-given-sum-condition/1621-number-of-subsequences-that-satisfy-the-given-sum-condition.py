'''
abcde
a
ab ac ad ae
abc abd abe  acd ace ade
abcd abde cde
abcde

a
ab ac ad 
abc abd acd
abcd
'''
mod = 10 ** 9 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n):
            tar = target - nums[i]
            right = bisect_right(nums ,  tar)
            if right <= i:
                continue
            
            tot = (right - i)

            ans = (ans % mod + pow(2 , tot  - 1 , mod)) % mod
        
        return ans % mod

        

