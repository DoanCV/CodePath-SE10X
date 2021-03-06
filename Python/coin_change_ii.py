"""
U
given an integer array coins representing coins of different values
and an integer amount representing a total amount of money

find the number of combinations that make up that amount
    how many ways can you get the amount with the coins
    
we have unlimited amount of each coins

M
We can see that there is overlapping subproblems

Base case: 1 way to get 0

PIR

E
O(N * M) time complexity where N is the total number of coin types that are given and M is the target.
O(M) space complexity since we are checking every amount below in a 1-D array.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0 for _ in range(amount + 1)]
        
        # base case
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]
        
        return dp[amount]
