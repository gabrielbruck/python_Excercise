#
# def build_pyramid():
#     num = int(input("How many rows:"))
#     if num <= 0:
#         print("Please enter a positive Number")
#     else:
#         for i in range (0,num):
#              for j in range(0,num-i-1):
#                 print(end="  ")
#              for j in range(0,2*i+1):
#                 print("*", end=" ")
#              print()
#
# build_pyramid()

def build_pyramid():
    num = int(input("How many rows:"))
    upordown = input("please type up or down:")
    if num > 0 and upordown == "up":
        for i in range (0,num):
             for j in range(0,num-i-1):
                print(end="  ")
             for j in range(0,2*i+1):
                print("*", end=" ")
             print()
    elif num > 0 and upordown == "down":
        for i in reversed(range(0, num)):
                for j in range(0, num - i - 1):
                    print(end="  ")
                for j in range(0, 2 * i + 1):
                    print("*", end=" ")
                print()
    else:
        print("Invalid")

build_pyramid()