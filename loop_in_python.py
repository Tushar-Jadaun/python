l=[1,"tushar","hello","happy","hii"]
print(type(l))
n=0
while(n<len(l)):
     print(l[n])
     n += 1
     
# pronlem first 
n = int(input("enter the number "))
for i in range (1,11):
     print(f"{n} X {i} = {n * i}") 

# problem secound
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")

# third problem
n= int(input("enter the number :"))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1
    
# problem fourth
n= int(input("enter the number :"))

for i in range(2,n):
    if((n%i)==0):
      {
        print("even number") 
          
      }
    else:
       {
        print("prime number")
       }    

# problem fifth
n= int (input("enter the number :"))

i=1
temp=0

while(i<=n):
    temp=i+temp
    i+=1
    
print(temp)


# problem six
n=int(input("enter the number :"))
temp =1

for i in range(1,n+1):
    temp = i * temp

    
    
print(temp)

# problem seven
n=int(input("enter :"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i,end="")
    print("\n")

# problem eight
n=int (input("enter :"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")
    if(i==1 or i==n):
        {
            print("*"*n,end="")
        } 
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="") 
    print("\n") 
    
n=int (input("enter :"))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")   
