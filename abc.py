str = "My Name is Aaradhya I am 29 years old flat no 204 Many more to come"
white_space_count = 0

for char in str:
    if char.isspace():
        white_space_count += 1

print("Number of white spaces:", white_space_count)
