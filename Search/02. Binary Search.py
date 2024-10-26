from common import words

words.sort()

def binary_search(iterable, target):
    tries = 0
    left, right = 0, len(iterable) - 1
    while left <= right:
        tries += 1
        mid = (left + right) // 2
        if iterable[mid] == target:
            return mid
        elif iterable[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


result = binary_search(words, "lesson")

if result != -1:
    print(words[result])
else:
    print("Not Found.")
