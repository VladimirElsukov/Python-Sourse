def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


selection_sorted = selection_sort([5, 3, 1, 4, 2])
print(selection_sorted)  # вывод: [1, 2, 3, 4, 5]





