name="Tushar"
print(name[1:3]) 
print(name[-3:-1])
print(name[:5])
print(name[2:])

# skip the value
number="0123456789"
print(number[0:9:2])
print(len(number)) #take the length
print(type(number)) #take the type 

#other operations
print(name.endswith("us"))
print(name.startswith("Tu"))
print(name.capitalize())

#escape sequence character
h="tushar is a good \n boy not a \"bad boy\""
print(h)


# set practice
#problem 1
enter =input("enter  your name : ")
print(f"Good morning {enter}")

#problem 2
letter =''' Dear <|Name|>,
            You are  Selected!
            <|Date|>'''
print(letter.replace("<|Name|>","Tushar").replace("<|Date|>","26/11/2005"))

#problem 3
space="tushar is a   good   boy  "
print(space.find("   "))

#problem 4
print(space.replace("   "," "))

#problem 5
print("Hey ,\n\ttushar is a good boy and\nit is not a bad boy")