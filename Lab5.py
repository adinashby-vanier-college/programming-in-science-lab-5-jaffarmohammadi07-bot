# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def random_ass_shape(n):
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

print(random_ass_shape(6))

# 1
# 12
# 123
# 1234
def number_pattern(n):
    return ""

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""
