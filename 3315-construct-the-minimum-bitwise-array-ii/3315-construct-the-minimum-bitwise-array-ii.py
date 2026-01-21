class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        '''
        eg-> 
        0000
        0001
        0010
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1010

        A = KTHBIT ON
        B = LAST K-1 BITS

        or just 1 bit change 

        

        '''

        ans = []
        for num in nums:
            N = num.bit_length()
            val = float("inf")
            for i in range(N + 1):
                temp = num & ~(1 << i)

                if temp | (temp + 1 )== num:
                    val = min(temp , val)
                if temp | (temp - 1) == num:
                    val = min(temp - 1 , val)
                


            ans.append(val if val != float("inf") else -1)

        return ans