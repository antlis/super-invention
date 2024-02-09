def decode(message_file):
    # reads every line from file provided
    with open(message_file, 'r') as file:
        lines = file.readlines()
    # eg
    # ['267 land\n', '274 sun\n', '34 too\n', etc...]

    # Creates empty dictionary called pyramid
    pyramid = {}

    # Loops over everyline stored in `lines` array
    for line in lines:
        # Line below removes line break (\n) - strip func
        # Then it splits line by white space, space between number and word
        # So you get soemthing like ['267', 'land']
        # Then you assign first array item to variable - num
        # And second item to variable word
        num, word = line.strip().split()

        # Here you assign `num` as dictionary index
        # And word as pyramid dictionary value
        # So your data structure looks like this
        # {
        #   267: 'land',
        #   274: 'sun',
        #   34: 'too',
        #   etc...
        # }
        # And you need integer to be your index, eg number
        # Cause after you split string, num is string, int converts it to number
        pyramid[int(num)] = word

    # Well obvisouly decoded_message is something that you gonna return from that function
    # It's empty for now
    decoded_message = ''

    # print(max(pyramid.keys()))
    # print(range(1, max(pyramid.keys()) + 1))
    # print(sorted(pyramid.keys()))

    # As you can see here is loop again
    # But this time it loops over range
    # It starts from 1
    # And ends by 301
    # Basically it's amount of keys in pyramid dictionary
    # Keys are numbers
    # So it's - [267, 274, 34, etc...]
    # Then you getting max value from that array of keys, which is 300
    # And then you loop over each value in that range
    # 1, 2, 3, 4, 5, etc...
    for i in sorted(pyramid.keys()):
        # print(i)
        # print(pyramid[i])
        # Here you write to decoded_message
        # Every word in that pyramid dictionary
        # You provide value from range
        # pyramid[1]
        # pyramid[2]
        # pyramid[3]
        # etc...
        # And you add white space after each word
        # In result you getting your final message
        decoded_message += pyramid[i] + ' '

    return decoded_message.strip()


# Example usage:
decoded_message = decode('input.txt')
print(decoded_message)

decoded_messages_2 = decode('input-2.txt')
print(decoded_messages_2)
