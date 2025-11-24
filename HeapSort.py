import heapq


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


heapsorted_arr = heapsort([5, 3, 1, 4, 2])
print(heapsorted_arr)  # вывод: [1, 2, 3, 4, 5]










