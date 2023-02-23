#Importing Modules
import string
import random
def login():

#Function for Captcha
    def captcha():
        N = 7
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        global cap
        cap=res
        print("The generated random string : " + str(res))
        
#Usernam and Password Validation using Captcha function 
    i=0
    while(i<3):
       user_name=input('Enter the user Name')
       password=input('Enter the Password')
       if(user_name==username and password==password1):
          print('Valid Credentials')
          transaction()
          break
       elif(user_name!=username and password!=password1):
           print('Invalid Credentials')
           i=i+1
           if(i==3):
               print('\n',' ***This is your last chance***')
               user_name=input('Enter the user Name')
               password=input('Enter the Password')
               captcha()
               d=input('Enter the above captcha')
               if(user_name==username and password==password1 and d==cap):
                   print('your password is correct')
               else:
                   print('Your Password is still Incorrect ','\n','Your Account is locked')
                   return None

#Transaction Function
def transaction():
    print("1-withdraw")
    print("2-balance enquiry")
    print("3-fast cash")
    c=int(input("please choose transactions:"))
    if(c==1):
        w=int(input("enter withdraw amount:"))
        if(w<=m and w%100==0):
            print("please take your amount:",w)
        else:
            print("invalid cash")
    elif(c==2):
        print("your available amount:",m)
    elif(c==3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        f=int(input("enter fast cash option:"))
        if(f==1 and 5000<m):
            print("please take cash 5000")
        elif(f==2 and 10000<m):
            print("please take cash 10000")
        elif(f==3 and 15000<m):
            print("please take cash 15000")
        elif(f==4 and 20000<m):
            print("please take cash 20000")
        else:
            print("invalid fast cash option")
    else:
        print('You Entered the Invalid option')
        
    
#Program with traction and Credentials Authentication
cnt=0
count=0
Name=''
cardno=0
pinno=0
username=''
password1=''
repass=0
cardno1=0
pinno1=0
m=0
print('Welcome to the Bank')
while(cnt<1):
    print('Select Customer login->1 or admin login->2')
    i=int(input(''))
    if(i==1):
        print('login->1 or for sign up->2')
        e=int(input(''))
        if(e==1):
            login()#calling Username and Password Function
        elif(e==2):
              Name=input('Enter the Name ')
              cardo=int(input('Please Enter the Card Number'))
              pinno=int(input('Please Enter the Card Pin Number'))
              m=int(input('please Enter the Deposit Amt'))
              username=input('Enter the user name ')
              password1=input('Enter the password ')
              repass=input('Re-enter the Password for confirmation ')
              if(password1==repass):
                  print('Your Information is saved')
                  print('Your Account has been Created successfully')
                  print('Please Enter the login details')
                  login()#calling Username and Password Function
                  print('Thank you for Banking with-us')
              else:
                  ('Password is not matched with confirmation')
        else:
            print('You Entered the Invalid option')
    elif(i==2):
        print("Please Sign up and enter the detials")
         
    else:
        print('You Have entered Invalid option')
            
       
