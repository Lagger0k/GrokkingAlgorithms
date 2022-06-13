def find_smallest(items: list) -> int:
    smallest = items[0]
    smallest_index = 0
    for i in range(1, len(items)):
        if items[i] < smallest:
            smallest = items[i]
            smallest_index = i
    return smallest_index


def selection_sort(items: list) -> list:
    sorted_items = []
    for i in range(len(items)):
        smallest_index = find_smallest(items)
        sorted_items.append((items.pop(smallest_index)))
    return sorted_items
