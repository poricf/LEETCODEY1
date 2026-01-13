class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        def check(c):
            above = 0
            below = 0
            for x,y,d in squares:
                ys = y
                ye = y + d
                # print(c , ys)
                if c <= ys:
                    above += d*d
                elif c >= ye:
                    below += d * d
                else:
                    y = abs(ye - c)
                    above += d * y
                    y = abs(ys - c)
                    below += d * y
                # print(below  , above , c)
            return below >= above

                


                
        left = 0
        right = 1e10
        eps = 1e-5
        while right - left > eps :
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        
        return left



