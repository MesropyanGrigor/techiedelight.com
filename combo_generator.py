def combinations(arr, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

# Define the array
array = [1, 2, 3, 4, 5]

# Generate combinations of three items
combinations_of_three = combinations(array, 3)

# Print the combinations
for combo in combinations_of_three:
    print(combo)
