def power(num: float, pow: float):
    if pow == 0:
        return 1
    if pow == 1:
        return num
    if num == 0:
        return 0
    if num == 1:
        return 1

    result = 1
    for _ in range(pow):
        result *= num

    return result


def radical(num: float):
    pass
