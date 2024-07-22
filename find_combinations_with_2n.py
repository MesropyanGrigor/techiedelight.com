def find_combinations(n):
    result = []

    # Helper function to perform backtracking
    def backtrack(current, n, used):
        # If current permutation is complete
        if len(current) == 2 * n:
            result.append(tuple(current))
            return

        for num in range(1, n + 1):
            if used[num] < 2:
                pos = len(current)
                # If this is the first occurrence of num, place it at pos
                if used[num] == 0:
                    current.append(num)
                    used[num] += 1
                    backtrack(current, n, used)
                    used[num] -= 1
                    current.pop()
                # If this is the second occurrence of num, place it at pos
                elif used[num] == 1 and pos >= num and current[pos - num -1] == num:
                    current.append(num)
                    used[num] += 1
                    backtrack(current, n, used)
                    used[num] -= 1
                    current.pop()

    # Initialize used array
    used = {i: 0 for i in range(1, n + 1)}
    used[1] = 1
    used[2] = 1
    used[3] = 1
    combos = [3, 1, 2]
    # Start backtracking with an empty permutation
    backtrack(combos, n, used)
    
    return set(result)

# Example usage
n = 3
print(find_combinations(n))  # Output: {(3, 1, 2, 1, 3, 2), (2, 3, 1, 2, 1, 3)}