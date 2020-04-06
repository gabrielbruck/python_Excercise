#4) Build function is_parsable(input)
#a) Possible types for input are int or string
#b) If input is of type int or if input can be parsed return true
#c) If input is not int or string or can not be parsed as int return false

def is_parsable(input):
    if isinstance(input, int) or input.isdigit() == True :
        print("True")
    else:
        raise ValueError ("False")


def second(input1):
    try:
        is_parsable(input1)
    except Exception as e:
        print(e.args[0])


second("4")
