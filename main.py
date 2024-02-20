# https://stackoverflow.com/questions/77843924/how-can-i-extract-the-last-word-from-each-row-of-a-pyramid/77844224#77844224

# arg file format
# 
# 1 i
# 2 something
# 4 else
# 3 love
# 5 dog
# 6 computers

# 1 (i)
# 2 3 (love)
# 4 5 6 (computers)

# Should reuslt in: i love computers

def decode(message_file):
    # https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
    # reads every line from file provided
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words_arr = map(str.strip, lines)

    width = 1  # number of items on the same line in the triangle
    last = 0   # index of the last item on the current line in the triangle

    # https://wiki.python.org/moin/Generators
    # https://www.w3schools.com/python/ref_func_map.asp
    # https://www.w3schools.com/python/ref_string_split.asp
    # !!! you need to turn key from string to integer with int(key)
    # if you wont do that, sorted function below won't work correctly
    # would consider string '10' go before string '9' for example
    words_generator = ((int(key), word) for key, word in map(str.split, words_arr))

    # https://www.w3schools.com/python/ref_func_sorted.asp
    words_sorted = sorted(words_generator)

    # https://pythonbasics.org/enumerate/
    words_enumerator = enumerate(words_sorted)

    #################################
    # in case you passing index-2.txt
    # 1 i - index 0
    # 2 something - index 1
    # 4 else - index 3 (because it's sorted)
    # 3 love - index 2
    # 5 dog - index 4
    # 6 computers - index 5

    #################################
    # i love computers
    # 1 (i)
    # 2 3 (love)
    # 4 5 6 (computers)
    #################################

    # -------------------------------
    # First iteration index == last | 0 == 0
    # you append first word - `i`, with index 0, to result_arr
    # then you assign new value to width, width = width + 1, width = 1 + 1, width = 2
    # also you assign new value to last, last = last + width, last = 0 + 2, last = 2
    # -------------------------------
    # Second iteration index 1 not equal last which is 2
    # -------------------------------
    # Thired iteration index == last | 2 == 2
    # you append word with idnex 2 to result array - love
    # then you assign new value to width, width = width + 1, width = 2 + 1, width = 3
    # also you assign new value to last, last = last + width, last = 2 + 3, last = 5
    # -------------------------------
    # Fourth iteration index 3 not equal last which is 5
    # -------------------------------
    # Fifth iteration index 4 not equal last which is 5
    # -------------------------------
    # Sixth iteration index == last | 5 == 5
    # you append word with idnex 5 to result array - computers
    # ......
    #################################

    # https://www.w3schools.com/python/python_iterators.asp
    # https://wiki.python.org/moin/Iterator
    # (_, word), underscore here is line key, which is not important, cause not used
    # We rely only on index
    result_arr = []
    for index, (_, word) in words_enumerator:
        if index == last:
            width = width + 1
            last = last + width
            result_arr.append(word)
            # print('i: ', + index)
            # print('_: ', + _)
            # print('word: ' + word)
            # print('width: ' + str(width))
            # print('last: ' + str(last))
            # print('-------------------')

        # Shorter version
        #
        # if index == last and (last := last + (width := width + 1)):
        #     result_arr.append(word)
            # print('i: ', + index)
            # print('_: ', + _)
            # print('word: ' + word)
            # print('width: ' + str(width))
            # print('last: ' + str(last))
            # print('-------------------')

    return " ".join(result_arr)

    # Shorter version
    #
    # return  " ".join(
    #     word for index, (_, word) in words_enumerator
    #     # Explanation of := operator
    #     # https://stackoverflow.com/questions/10405820/what-is-the-operator
    #     if index == last and (last := last + (width := width + 1))
    # )

print('\n')
print('input-2.txt result: ')
print('-------------------')
print(decode('input-2.txt'))
print('-------------------')
print('\n')
print('input.txt result: ')
print('-------------------')
print(decode('input.txt'))
print('-------------------')
print('\n')
