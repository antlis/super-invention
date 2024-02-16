def decode(message_file):
    # reads every line from file provided
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words_arr = map(str.strip, lines)

    width = 1  # number of items on the same line in the triangle
    last = 0   # index of the last item on the current line in the triangle

    # https://pythonbasics.org/decorators/
    words_generator = ((int(key), word) for key, word in map(str.split, words_arr))

    words_sorted = sorted(words_generator)

    # https://pythonbasics.org/enumerate/
    words_enumerator = enumerate(words_sorted)

    # for i in words_enumerator:
    #     print(i)

    # print(words_enumerator)

    return  " ".join(
        word
        for i, (_, word) in words_enumerator
        # Explanation of := operator
        # https://stackoverflow.com/questions/10405820/what-is-the-operator
            if i == last and (last := last + (width := width + 1))
    )


# decode('input.txt')
print(decode('input.txt'))
