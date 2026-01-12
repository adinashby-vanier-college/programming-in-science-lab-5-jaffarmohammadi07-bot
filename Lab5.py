def hollow_square(n):
    result = ""
    i = 0

    while i < n:
        if i == 0 or i == n - 1:
            j = 0
            while j < n:
                result += "*"
                j += 1
        else:
            result += "*"
            j = 0
            while j < n - 2:
                result += " "
                j += 1
            result += "*"

        if i != n - 1:
            result += "\n"
        i += 1

    return result


def number_pattern(n):
    result = ""
    i = 1

    while i <= n:
        j = 1
        while j <= i:
            result += str(j)
            j += 1

        if i != n:
            result += "\n"
        i += 1

    return result


def sum_of_natural_numbers(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    return total


def centered_star_pyramid(n):
    result = ""
    i = 0

    while i < n:
        spaces = 0
        while spaces < n - i - 1:
            result += " "
            spaces += 1

        stars = 0
        while stars < 2 * i + 1:
            result += "*"
            stars += 1

        if i != n - 1:
            result += "\n"
        i += 1

    return result
