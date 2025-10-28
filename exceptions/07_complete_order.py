class InvaildChaiError(Exception): pass

def bill(flavor,cups):
    menu = {"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvaildChaiError("that chai is not available")
        if not isinstance(cups,int):
            raise TypeError("That quantity is not available")
        
        total =menu[flavor] * cups
        print(f"your bill for {cups} cups of {flavor} chai : rupees{total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("order is completed")    
        
bill("masala",2)
bill("masala","two")
bill("ginger",2)        