# dictinory methods
marks ={"harray":100,
        "tushar":98,
        "Rohit":58
        }
print(type(marks),marks)
print(marks.items())
print(marks.values())
print(marks.keys())
marks.update({"Rohit":45})
print(marks.items())
print(marks.get("tushar"))


# set method
s={5,5,5,2,4,15,1,5,8,2,"tushar"} #declration
print(s.add(45)) #to add
print(s) #print
print(type(s))  # check the type
print(len(s))   # length 
s.remove("tushar")  #remove
print(s)
s1={1,5,9,2,5,3}
print (s.union(s1))  #union
print(s.intersection(s1))   #intersection


# problem 
# problem no.1
word={
        "Happy":"khush",
        "sad":"dukhi",
        "how are you" : " kese ho tum ",
        "nice":"bahut badiya"
}
words=input("enter the input :")
print(word[words])

# problem 2
s=set()
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
n=int(input("inter input"))
s.add(n)
print(s)


# problem 3
t=set()
t.add(20)
t.add('20')
print(t)


# problem 4
s= set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))

s={}
name=input("enter the name :")
lang=input("enter the language :")
s.update({name:lang})
name=input("enter the name :")
lang=input("enter the language :")
s.update({name:lang})
name=input("enter the name :")
lang=input("enter the language :")
s.update({name:lang})
name=input("enter the name :")
lang=input("enter the language :")
s.update({name:lang})
print(s)