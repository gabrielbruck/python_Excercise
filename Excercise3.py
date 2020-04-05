#Build function is_even(number)
#a) Returns true if number is even, otherwise false
#b) Number should be integer, if not, display a meaningful msg and exit


def is_even(number):
    if type(number) == int:
        if number % 2 == 0:
            print ("true")
            return True
        else:
            print ("false")
            return False
    else:
        print("that's not valid")
is_even(45)

