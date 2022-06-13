def quick_sort(numbers: list) -> list:
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]
        less = [i for i in numbers[1:] if i < pivot]
        greater = [i for i in numbers[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
