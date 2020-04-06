def change_words_starting_with_a(list_to_check):
    try:
        return [x + "hello" if x[0] == "a" else x for x in list_to_check]
    except TypeError as e:
        print("caught type error")

name = ["apple","banana","world","abraham"]
print(change_words_starting_with_a(name))

