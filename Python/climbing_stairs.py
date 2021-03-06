"""
U
There are N steps in our staircase

We can only climb 1 or 2 steps

We need to find out how many ways are there to climb to the top of our staircase


M
Lets say N = 5
So this is our staircase:
                5
            4
        3
    2 
1
To get to step 5, the previous step can only be from step 3 or step 4 since we can only move up one or two steps at a time
So if we know how many ways there are to get to step 3 and step 4 then we figured out how to get to step 5

If we structure our observation as a tree we see the following

                    5
            3               4
        1       2       2       3 
     0        0   1   0   1   1   2
                 0       0   0   1 0
                                0
If we used simple recursion, we would have repeated a lot of calculations
Instead we can use dynamic programming

We can reuse steps that we calculated
Base case:
    There is only 1 way to get to step 1
    There is only 1 way to get to step 0

P
For now lets try top down
There is only one parameter steps so we will use a 1-D array to keep track of previous calculations

the recurrence relation is actually the fibonacci sequence: f(n) = f(n-1) + f(n-2)

IR

E
O(N) time complexity where N is n or the number of steps
O(N) space complexity since we store the number of ways to get to steps 0 to N in an array of size N + 1.
"""

# Top Down
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        return self.recurse(n, dp)
    
    def recurse(self, n, dp):
        if dp[n] > 0:
            return dp[n]
        
        ways = self.recurse(n - 1, dp) + self.recurse(n - 2, dp)
        dp[n] = ways
        return ways

      
# Great let's try bottom up, which will be an iterative take
  # instead of a tree we can think of it like an array where each index is a step and the value is the number of ways we can get to that step

#  0  1  2  3  4  5
# [1, 1, 2, 3, 5, 8]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
