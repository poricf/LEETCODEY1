class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        mp = {}
        x = -1
        for c in num:
            if c != '9':
                x = c
                break
        y = num[0]
        mx = []
        mn = []
        for c in num:
            mx.append(c if c != x else '9')
            mn.append(c if c != y else '0')
        
        return int("".join(mx)) - int("".join(mn))
