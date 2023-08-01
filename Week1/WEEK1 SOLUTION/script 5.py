#writw  a python script to enter any  string and count vowels
def input_vowels(string):
    x=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vowels:
            x+=1
    print(f"vowels is in the string are{x}")
string=input("\n Enetr string....?:")
input_vowels(string)          
