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
    # reads every line from file provided
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words_arr = map(str.strip, lines)

    width = 1  # number of items on the same line in the triangle
    last = 0   # index of the last item on the current line in the triangle

    # https://www.w3schools.com/python/python_iterators.asp
    # https://wiki.python.org/moin/Iterator
    words_generator = ((int(key), word) for key, word in map(str.split, words_arr))

    words_sorted = sorted(words_generator)

    # https://pythonbasics.org/enumerate/
    words_enumerator = enumerate(words_sorted)

    result_arr = []

    for i, (_, word) in words_enumerator:
        if i == last and (last := last + (width := width + 1)):
            result_arr.append(word)
            # print('i: ', + i)
            # print('_: ', + _)
            # print('word: ' + word)
            # print('width: ' + str(width))
            # print('last: ' + str(last))
            # print('-------------------')

    return " ".join(result_arr)

    # return  " ".join(
    #     word for i, (_, word) in words_enumerator
    #     # Explanation of := operator
    #     # https://stackoverflow.com/questions/10405820/what-is-the-operator
    #     if i == last and (last := last + (width := width + 1))
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
