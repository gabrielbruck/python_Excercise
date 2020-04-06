def name_checker(list_of_names):
    for i in list_of_names:
        if " " not in i:
            yield i

list = ["gabriel bruck", "Ben", "rommi englard", "Jon Smith", "Dennis"]
last_names = name_checker(list)
for i in last_names:
    print(i)
