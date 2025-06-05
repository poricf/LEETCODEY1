class UnionFind:
    def __init__(self , n):
        self.parents = list(range(n + 1))
    
    def union(self , u , v):
        # find rood of both
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False
        if root_u > root_v:
            self.parents[root_u] = root_v
        else:
            self.parents[root_v] = root_u

        return True
    def find(self , u):
        # find root of u
        root = u

        while self.parents[root] != root:
            root = self.parents[root]

        # path compression to be implemented

        return root





class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        
        uf = UnionFind(26)

        for i in range(len(s1)):
            u , v = s1[i] , s2[i]
            uf.union(ord(u) - 97 , ord(v) - 97)
        
        ans = []
        for c in baseStr:
            smallest = uf.find(ord(c) - 97)
            ch = chr(smallest + 97)
            ans.append(ch)
        
        return "".join(ans)
        