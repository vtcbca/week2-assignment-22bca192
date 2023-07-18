#write a python script to enter any number and check aemstrong


def check_armstrong(n):
    cp=n
    sum=0
    while(n>0):
        d=n%10
        re=d*d*d
        sum=sum+re
        n=n//10
     if cp==sum:
        print('Entered number is armstrong  number')
     else:
        print('Enetered number is not armstrong number:')
n=int(input("enter any number:"))
check_palidrome(n)            
        
