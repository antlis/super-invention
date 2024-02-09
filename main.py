def decode(message_file):
    # reads every line from file provided
    with open(message_file, 'r') as file:
        lines = file.readlines()

    words_arr = map(str.strip, lines)

    width = 1  # number of items on the same line in the triangle
    last = 0 # index of the last item on the current line in the triangle
    return  " ".join(
        word
        for i, (_, word) in enumerate(
            sorted((int(a), b) for a, b in map(str.split, words_arr))
        )
        if i == last and (last := last + (width := width + 1))
    )

print(decode('input-2.txt'))
