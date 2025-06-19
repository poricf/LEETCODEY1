class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][state] -> for each day i with decision of making state what is the max profit we can get
        '''
        1 , 2 , 0 , 5 , 6
        lets take this as an example
        dp
        sell , hold , rest
        
        [(0,-1,0) ]

        at first this is our answer because we cant sell , if we hold we must buy so -1 and if we rest do noting = 0

        then to update the next states
        to sell means we were holding and now we added the price of today 
        to hold means 
        either we were holding yesterday to 
        orelse
        we sold day before yesterday we rest yesterday and we bought today

        and we rest today means 
        either we sold yesterday or we rest yesterday
        '''

        dp = [[0 , 0 , 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]


        for i in range(1 , len(prices)):
            dp[i][0] = dp[i - 1][1] + prices[i]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])
            dp[i][2] = max(dp[i - 1][0] , dp[i - 1][2])
        
        return max(dp[-1])
