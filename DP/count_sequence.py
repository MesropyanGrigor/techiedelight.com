def count_sequences(n):
    if n == 0:
        return 0

    # Define the keypad adjacency matrix
    adj = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }

    # Initialize dp table
    dp = [{str(i): 1 for i in range(10)}]

    for i in range(1, n):
        new_dp = {str(i): 0 for i in range(10)}
        for key in dp[i-1]:
            for neighbor in adj[key]:
                new_dp[neighbor] += dp[i-1][key]
        dp.append(new_dp)

    return sum(dp[n-1].values())


count_sequences(12)