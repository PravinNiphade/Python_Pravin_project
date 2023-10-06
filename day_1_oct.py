str = "My Name is Aaradhya I am 29 years old flat no 204 Many more to come"
Total_words = str.split()
count = len(Total_words)
print(Total_words)
print("total words ", count)
white_space = 0
total_digit = 0
total_character = 0
for i in Total_words:
     if(i[0] == "M"):
       print("word starts with M ::" ,i)

for char in str:
    if char != ' ':
        total_character += 1


    if char.isspace():
        white_space += 1

    if char.isdigit():
        total_digit += 1
print("total digit ::", total_digit)
print("Total white spaces = ", white_space )
print("total_character " , total_character)






