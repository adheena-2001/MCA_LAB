def add_ing_ly(input_string):
    if input_string.endswith('ing'):
        result_string=input_string + 'ly'
    else:
        result_string = input_string + 'ing'
    return result_string
input_string = input("enter a string:")
modified_string = add_ing_ly(input_string)
print("modified string:", modified_string)
