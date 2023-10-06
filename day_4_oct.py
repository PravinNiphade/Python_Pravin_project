user_input = input("Enter character :: ")

if len(user_input) !=1:
    print("enter character whose length is one ")

else:
    ASCII_VALUE = ord(user_input)

    print("Ascii value of {} is :: {}".format(user_input, ASCII_VALUE))