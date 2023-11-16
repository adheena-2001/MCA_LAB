input_string=input("enter the string:")
char_frequency={}
for char in input_string:
    char_frequency[char]=char_frequency.get(char, 0) + 1
print("character frequencies in the string:")
for char, frequency in char_frequency.items():
    print((char),(frequency))
