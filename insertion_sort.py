

def insertion_sort(array):

    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[i]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]







array = [5, 4, 3, 2, 1, -1]

insertion_sort(array)

print(array)
