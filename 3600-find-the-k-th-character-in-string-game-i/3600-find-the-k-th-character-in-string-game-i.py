class Solution:
    def kthCharacter(self, k: int) -> str:

        def generate(n):
            if n == 1:
                return ["a"]
            
            prev = generate(n//2)

            temp = []
            for c in prev:
                nw = (((ord(c) - 97) + 1) % 26) + 97
                temp.append(chr(nw))
            
            return prev + temp

        n =  2 ** ceil(log2(k))
        res = generate(n)
        print(res)
        return res[k - 1]