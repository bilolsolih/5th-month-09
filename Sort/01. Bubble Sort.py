from common import words

numbers = [9, 5, 0, 19, 87, 103, 1, 4, 9, 7, 23, 45, 67, 89, 0.2, 91, 77]


def bubble_sort(iterable):
    n = len(iterable)
    for i in range(n):
        for j in range(0, n - i - 1):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]

    return iterable

numbers = bubble_sort(numbers)
print(numbers)

