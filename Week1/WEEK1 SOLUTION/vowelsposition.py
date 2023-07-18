# write apyhon script to enter any sting .replace vowels with its position number.

def string_vowels_position(string):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    n_string=""

    for i,char in enumerate(string):
        if char in vowels:
            n_string += str(i)
        else:
            n_string += char
    return n_string            
            
user_input=input("enter any name:")

answer=string_vowels_position(user_input)

print("THE VOWELS WITH STRING IS:",answer)
    
