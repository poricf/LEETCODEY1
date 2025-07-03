class Solution:
    def kthCharacter(self, k: int) -> str:
        '''
        a
        ab
        abbc
        abbcbccd
        1 - 1
        2 - 2
        34 - 3
        45678 - 4
        910111213141516 - 5

        n = ceil(log(16)) + 1 
        '''

        n = ceil(log2(16)) + 10
        def generate(n):
            if n == 1:
                return "a"
            
            prev = generate(n - 1)
            new = ""
            for c in prev:
                new += chr((((ord(c) + 1) - 97) % 26) + 97) 
            return prev + new

        ans = generate(n)

        return ans[k - 1]

