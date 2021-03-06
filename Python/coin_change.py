"""
U
We have unlimited of each coin
We need to find the fewest number of coins to make the given amount

M
Base cases
    Smallest number of coins that we need for 0 coins
    Smallest number of coins that we need for 1 coin

Bottom up

P
dp array for us to store the best answer

IRE


"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # intially set everything in dp array with something invalid
        dp = [amount + 1 for _ in range(amount + 1)]
        
        # 0 coins to make 0 amount
        dp[0] = 0
        
        ### sort the coins for optimization see note below
        coins.sort()
        
        for i in range(amount + 1):
            for j in range(len(coins)):
                
                # if we can take the coin, do it
                if coins[j] <= i:
                    # we want the fewest amount of coins
                    # account for taking out the coin, find the best way be accessing the dp array
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
                
                ### optimization: if the coins are sorted then we can stop checking since our coins are too big
                else:
                    break
                
        if dp[amount] > amount:
            return -1  
        else:
            return dp[amount]
        
# O(N*M) time complexity, where N is the length of the coins array and M is our amount, since we loop through each coin and each amount up to the given amount.
# O(M) space complexity since that is the size of our dp array to store subproblems.
