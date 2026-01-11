# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(n):
        if i == 0 or i == n - 1:
            for k in range(n):
                result += "*"

        else:
            result += "*"
            for j in range(n-2):
                result += " "
            result += "*"
        result += "\n"


    return result.rstrip()

print(hollow_square(6))

# 1
# 12
# 123
# 1234
\
def number_pattern(n):
    result = ""

    for i in range(1,n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result += "\n"
    
    return result.rstrip()
print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def center_star_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n - i - 1):
            result += " "
        for k in range(2 * i + 1):
            result += "*"
        result += "\n"

    return result.rstrip()
print(center_star_pyramid(4))
