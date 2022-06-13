def binary_search(items: list, searching_item: int) -> int or None:
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]
        if guess == searching_item:
            return mid
        elif guess < searching_item:
            low = mid + 1
        else:
            high = mid - 1
    return None
