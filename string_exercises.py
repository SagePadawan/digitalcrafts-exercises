a_string = "abracadabra"
# print(a_string.upper())
# print(a_string.title())
user_string = ""
string_length = len(a_string)

#print (string_length)
for i in range(string_length - 1, -1, -1):
    user_string += a_string[i]
print (user_string)
