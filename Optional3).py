def solve_math(string, *numbers):
    string = string.replace("x", "%d")
    print(string % numbers, " = ", eval(string % numbers))


solve_math("x * x - x / x + x", 1, 2, 3, 4, 5)
