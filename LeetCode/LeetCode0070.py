#Fibonacci

def climb_stairs(n):
    if n <= 2:
        return n

    # Create an array to store the number of ways to reach each step
    # We add 1 to the size of the array to accommodate steps from 0 to n
    dp = [0] * (n + 1)

    # There's one way to reach step 0 (by not taking any step)
    dp[0] = 1

    # There's one way to reach step 1 (by taking one step)
    dp[1] = 1

    # There are two ways to reach step 2 (by taking one step twice or two steps once)
    dp[2] = 2

    # Calculate the number of ways to reach each step from step 3 to n
    """For each step i, we can reach it by either taking one step from step i-1 (since we can take only 1 or 2 steps at a time) or by taking two steps from step i-2. 
    So, the total number of ways to reach step i is the sum of the ways to reach step i-1 and step i-2."""
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
