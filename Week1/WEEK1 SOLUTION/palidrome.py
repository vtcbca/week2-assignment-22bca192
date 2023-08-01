#write a script to enter any number and check palidrome or not.


def check_palidrome(n):
    cp=n
    re=0
    if n:
        while(n>0):
            d=n%10
            re=re*10+d
            n=n//10
        print(f'reverse number{re}')
        if cp==re:
             print('Entered number is palidrome number')
        else:
            print('Enetered number is not palidromenumberelse:')
    else:              
       print('Entered number is not integer number')
n=int(input("enter any number:"))
check_palidrome(n)            
        
