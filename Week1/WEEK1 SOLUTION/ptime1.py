# write apython script and  check   the number prime or not.

def check_prime(no):
    for i in range(2,no,no):
        if no%i=0:
            print(f'{no}is not prime number')
            break
        else:
            print(s'{no}is prime number')
no=int(input("enter any number:"))
check_prime(no)
            
            
