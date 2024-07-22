


def combination(array, k):
    def back_track(start, path):
        if len(path) == k:
            results.append(tuple(path[:]))
            return

        #result = []
        for i in range(start, len(array)):
            path.append(array[i])
            back_track(i + 1, path)
            path.pop()

    results = []
    back_track(0, [])
    return results


combos = combination([1, 2, 3, 4, 5], 3)
for combo in combos:
    print(combo)
#print(combos)

from itertools import combinations

combos_s = combinations([1, 2, 3, 4, 5], 3)
print(list(combos_s))