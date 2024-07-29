def rod_cutting(n, price):
    # Initialize the dp array
    dp = [0] * (n + 1)
    
    # Fill the dp array using the bottom-up approach
    for i in range(1, n + 1):
        max_val = float('-inf')  # Initialize max_val to negative infinity for the current rod length i
        for j in range(1, i + 1):
            # Update max_val with the maximum value of either current max_val or the new computed value
            max_val = max(max_val, price[j - 1] + dp[i - j])
            
        dp[i] = max_val  # Store the computed maximum profit for rod length i in dp[i]
    
    return dp[n]  # The last element in dp array will have the maximum profit for rod length n




# Example usage
n = 4
price = [1, 5, 8, 9, 10, 17, 17, 20]
print(rod_cutting(n, price))  # Output: 10


def rod_cutting_recursive(n, price):
    # Base case: if the length of the rod is 0, the maximum profit is 0
    if n == 0:
        return 0
    
    max_val = float('-inf')  # Initialize max_val to negative infinity
    
    # Recursively calculate the maximum profit by making cuts
    for i in range(1, n + 1):
        max_val = max(max_val, price[i - 1] + rod_cutting_recursive(n - i, price))
        # n -1, n-2, n - 3, n - 4 .... 1
        # n = 1, i = 1 max_value = max(float("-inf"), 1 + 0)
    
    return max_val


# i = 1, max(max_val, price[0] + rod_cutting_recursive(n, price))
# i = 2, price[1] + rod_cutting_recursive(1, price)
#
#