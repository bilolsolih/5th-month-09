from common import numbers, words

def quick_sort(iterable):
    if len(iterable) <= 1:
        return iterable
    pivot = iterable[len(iterable) // 2]
    left = [x for x in iterable if x < pivot]
    middle = [x for x in iterable if x == pivot]
    right = [x for x in iterable if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


print(numbers)
numbers = quick_sort(numbers)
print(numbers)
