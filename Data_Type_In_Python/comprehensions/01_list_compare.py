menu =[
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

hot_tea = [my_tea for my_tea in menu if len(my_tea)>10]
print(hot_tea)