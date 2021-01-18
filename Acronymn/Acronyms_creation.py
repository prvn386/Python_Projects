user_input = str(input("Enter the string:"))
text = user_input.split() # creating list of words after splitting the user input
# print(text)
ac = "" # defining an empty string
for x in text:
    ac = ac + str(x[0]).upper()
print(ac) # printing the final acronymn
