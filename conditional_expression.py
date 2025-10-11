# first problem(Write a program to find the greatest of four numbers entered by the user. )
first=int(input("enter the first number :"))
secound=int(input("enter the secound number :"))
third=int(input("enter the third number :"))
fourth=int(input("enter the fourth number :"))
if(first>secound and first>third and first>fourth):
    {
        print("first is greater")
    }
elif(secound>first and secound>third and secound>fourth):
    {
        print("secound number is greater")
    }    
elif(third>first and secound<third and third>fourth):
    {
        print ("third number is greater")
    }  
else:
    {
         print ("fourth number is greater")
    }      

# secound problem (Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user)
first=int(input("enter the first number :"))
secound=int(input("enter the secound number :"))
third=int(input("enter the third number :"))

total_percentage=(100*(first+secound+third))/300
if(total_percentage>=40 and first>=33 and secound>=33 and third>=33):
    {
        print("pass",total_percentage)
    }
else:
    {
        print ("not pass")
    }


# third problem
# ( A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. )
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("enter the message")
if(p1 in message and p2 in message and p3 in message and p4 in message):
    {
        print("this content is spam")
    }
else:
    {
        print("this comment not spam")
    }    

# fourth problem
# (Write a program to find whether a given username contains less than 10 
# characters or not.)
name=input("enter the user name :")
if(len(name)<=10):
    {
        print("user name is to shandt ")
    }
else:
    {
        print("all is well")
    }

# fifth problem
# ( Write a program which finds out whether a given name is present in a list or not)
l1=["tushar","ravi","alok","devang","vinay"]
name=input("enter the name :")

if(name in l1 ):
    {
        print("it is present ")
    }
else:
    {
        print("not present")
    }    

# sixth problem
# ( Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50=> F )
marks=int(input("enter the number"))
if(marks>=90 and marks<=100):
    {
        print("EX")
    }
elif(marks>=80 and marks<=90):
    {
        print("A")
    } 
elif(marks>=70 and marks<=80):
    {
        print("B")
    }       
elif(marks>=60 and marks<=70):
    {
        print("C")
    }
elif(marks>=50 and marks<=60):
    {
        print("D")
    }   
else:
    {
        print("F")
    }     