def process_order(item,quantity):
    try:
        price = {"masala":20}[item]
        cost = price*quantity
        print(f"total cost is {cost} ")
    except KeyError:
        print("Sorry that's a key error");
    except TypeError:
        print("Sorry that's a Type error");        
        
process_order("masala","two")
process_order("masala",2)
process_order("ginger",3)        