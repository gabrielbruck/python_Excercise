import math

def list_square_even_power_odd(list_range):
    try:
        power_odd = [x**2 for x in range(list_range) if x % 2 != 0]
        square_even = [math.sqrt(x) for x in range(list_range) if x % 2 == 0]
        print('The Power of the  Odd numbers in this list are' + str(power_odd))
        print('The square root of the even numbers in this list are' + str(square_even))
    except TypeError as e:
        print("caught type error")
    except NameError as e:
        print("caught name error")

list_square_even_power_odd(5)


