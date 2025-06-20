class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cc = Counter(s)

        longt = 0
        lat = 0

        nlong = 0
        nlat = 0

        mxlat1 = 0
        mxlong1 = 0
        mxlat2 = 0
        mxlong2 = 0
        mxlat3 = 0
        mxlong3 = 0
        mxlat4 = 0
        mxlong4 = 0
        ans = 0
        ok = k
        

        ok1 = k
        ok2 = k

        along = 0
        alat = 0

        blong = 0
        blat = 0

        for c in s:
            if c == "N":

                if ok > 0:
                    nlong += 1
                    ok -= 1
                else:
                    nlong -= 1
                if ok2 > 0:
                    blong += 1
                    ok2 -= 1
                else:
                    blong -= 1

                longt += 1
                along += 1 
                
            elif c == "S":
                if ok1 > 0:
                    along += 1
                    ok1 -= 1
                else:
                    along -= 1
                
                if k > 0:
                    longt += 1
                    k -= 1
                else:
                    longt -= 1
                nlong += 1
                blong += 1
            elif c == "W":
                if ok > 0:
                    ok -= 1
                    nlat += 1
                else:
                    nlat -= 1
                if ok1 > 0:
                    ok1 -= 1
                    alat += 1
                else:
                    alat -= 1
                lat += 1
                blat += 1
            else:
                if k > 0:
                    lat += 1
                    k -= 1
                else:
                    lat -= 1
                if ok2 > 0:
                    blat += 1
                    ok2 -= 1
                else:
                    blat -= 1
                nlat += 1
                alat += 1

            ans1 = alat + along
            ans2 = blat + blong
            ans3 = nlat + nlong
            ans4 = lat + longt

            ans = max(ans ,ans1 , ans2 , ans3 , ans4)

        return ans