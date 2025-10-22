favourite_chai = [
    "Masala Chai ",
    "Green Tea ",
    "Masala Tea ",
    "Lemon Tea ",
    "Elaichi chai"
]
unique_chai = { my_chai for my_chai in favourite_chai}
print(unique_chai)




recipes = {
    "Masala Chai":["ginger","cardamom","clove"],
    "Elaichi Chai":["cardamom","milk"],
    "Spicy Chai":["ginger","black pepper","clove"]
}
unique_recipe = {spice for ing in recipes.values() for spice in ing}
print(unique_recipe)