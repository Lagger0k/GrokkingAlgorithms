def factorial(number: int) -> int:
    if number == 1:
        return number
    else:
        return number * factorial(number-1)
