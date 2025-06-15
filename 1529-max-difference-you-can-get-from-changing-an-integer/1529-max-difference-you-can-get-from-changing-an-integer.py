class Solution:
    def maxDiff(self, num: int) -> int:
        x = -1

        num = str(num)

        for c in num:
            if c!='9':
                x = c
                break
        
        mx = []
        for c in num:
            if c == x:
                mx.append('9')
            else:
                mx.append(c)

        x = -1
        first = num[0]
        mn = []
        if first != '1':
            for c in num:
                if c == first:
                    mn.append('1')
                else:
                    mn.append(c)
            
            return int("".join(mx)) - int("".join(mn))
        else:
            for c in num:
                if c != '1' and c != '0':
                    x = c
                    break
        
        for c in num:
            if c == x:
                mn.append('0')
            else:
                mn.append(c)
    
        
        return int("".join(mx)) - int("".join(mn))

            
