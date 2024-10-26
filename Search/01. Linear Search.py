from common import words


def linear_search(iterable, target):
    tries = 0
    for index, value in enumerate(iterable):
        tries += 1
        if value == target:
            print(tries)
            return index
    print(tries)
    return -1


result = linear_search(words, "badabum")

if result != -1:
    print(words[result])
else:
    print("Not Found.")
