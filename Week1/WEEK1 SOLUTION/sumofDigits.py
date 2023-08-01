#write a python script to enter any number and print sum of its digits.

a=int(input("enter any number:"))
sum=0
no=a
while(a!=0):
    sum=sum+a%10
    a=a//10
print("sum of digits of{}is{}".format(no,sum))    
    
      
