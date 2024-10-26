from common import numbers

def selection_sort(iterable):
    n = len(iterable)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if iterable[j] < iterable[min_idx]:
                min_idx = j
        iterable[i], iterable[min_idx] = iterable[min_idx], iterable[i]  # Eng kichkina elementni o'rnini almashtirish
    return iterable

print(numbers)
numbers = selection_sort(numbers)
print(numbers)